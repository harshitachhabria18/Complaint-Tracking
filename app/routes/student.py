from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os
from datetime import datetime, timedelta
from app.forms import ComplaintForm, FeedbackForm
from app.models import Complaint, Teacher, db, ComplaintHistory, Notification, Feedback
from random import choice
import uuid
from flask import current_app


bp = Blueprint('student', __name__, url_prefix='/student')

@bp.route('/new-complaint', methods=['GET', 'POST'])
@login_required
def new_complaint():
    form = ComplaintForm()

    if form.validate_on_submit():
        evidence_path = None
        evidence_paths = []

        if form.evidence.data:
            files = form.evidence.data
            if not isinstance(files, list):
                files = [files]  # wrap single file in list
            for file in files:
                if file and file.filename:
                    ext = os.path.splitext(file.filename)[1]
                    filename = f"{uuid.uuid4().hex}{ext}"
                    filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
                    file.save(filepath)
                    evidence_paths.append(f"uploads/{filename}")  # relative to 'static'

        evidence_path = ','.join(evidence_paths) if evidence_paths else None
        # if evidence_paths:
        #     evidence_path = ','.join(evidence_paths)

        # determine severity
        severity = "Urgent" if form.urgent.data else "Normal"

    # find teacher by category (active only)
        teachers = Teacher.query.filter_by(
            category=form.category.data, 
            is_active=True
        ).all()

        assigned_teacher_id = choice(teachers).id if teachers else None

        # compute deadline
        if severity == "Urgent":
            deadline = datetime.utcnow() + timedelta(days=2)  # urgent: 2 days
        else:
            deadline = datetime.utcnow() + timedelta(days=5)  # normal: 5 days

        # create complaint record
        complaint = Complaint(
            student_id=current_user.id,
            title=form.title.data,
            category=form.category.data,
            description=form.description.data,
            evidence_path=evidence_path,
            anonymous=form.anonymous.data,
            severity=severity,
            updates_email=form.updates_email.data,
            assigned_teacher_id=assigned_teacher_id,
            deadline=deadline,
            created_at=datetime.utcnow()
        )

        db.session.add(complaint)
        db.session.commit()

        history = ComplaintHistory(
            complaint_id=complaint.id,
            status=complaint.status,
            remarks="Complaint submitted",
            changed_by=current_user.id
        )
        db.session.add(history)

        notif = Notification(
            user_id=current_user.id,
            message=f"Your complaint #{complaint.id} has been submitted successfully."
        )
        db.session.add(notif)

        db.session.commit()


        flash("Complaint submitted successfully!", "success")
        return redirect(url_for('student.new_complaint'))

    return render_template('student/new_complaint.html', form=form)



@bp.route('/')
@login_required
def home():
    if current_user.is_authenticated:
    # Complaint stats
        total_pending = Complaint.query.filter_by(student_id=current_user.id, status="Pending").count()
        total_inprogress = Complaint.query.filter_by(student_id=current_user.id, status="InProgress").count()
        total_resolved = Complaint.query.filter_by(student_id=current_user.id, status="Resolved").count()
        total_urgent = Complaint.query.filter_by(student_id=current_user.id, severity="Urgent").count()

        # Latest complaints (limit 5)
        complaints = Complaint.query.filter_by(student_id=current_user.id).order_by(Complaint.created_at.desc()).limit(5).all()

        # Notifications (limit 5)
        notifications = Notification.query.filter_by(user_id=current_user.id).order_by(Notification.created_at.desc()).limit(5).all()

        return render_template(
            'student/dashboard.html',
            pending=total_pending,
            inprogress=total_inprogress,
            resolved=total_resolved,
            urgent=total_urgent,
            complaints=complaints,
            notifications=notifications
        )

@bp.route('/complaint-history')
def complaint_history():
    # Fetch complaints of current student with latest status
    complaints = Complaint.query.filter_by(student_id=current_user.id) \
        .order_by(Complaint.created_at.desc()).all()
    
    # build history JSON in Python, not Jinja
    for c in complaints:
        c.history_json = [
            {
                "status": h.status,
                "remarks": h.remarks,
                "changed_at": h.changed_at.strftime("%b %d, %Y")
            }
            for h in c.history
        ]
    
    return render_template(
        'student/complaint_history.html',
        complaints=complaints
    )

@bp.route('/complaint-detail')
@login_required
def complaint_detail():
    # Fetch latest complaint of logged-in student
    complaint = Complaint.query.filter_by(student_id=current_user.id)\
                               .order_by(Complaint.created_at.desc())\
                               .first_or_404()

    # Student info (direct from current_user)
    student = current_user

    # Assigned teacher (name or "Not Assigned")
    teacher = complaint.assigned_teacher.user.name if complaint.assigned_teacher else "Not Assigned"

    # Complaint history (ordered updates)
    history = ComplaintHistory.query.filter_by(complaint_id=complaint.id)\
                                    .order_by(ComplaintHistory.changed_at.asc()).all()

    # Priority mapping (Urgent → High, Normal → Normal)
    if complaint.severity == "Urgent":
        priority = "High"
    else:
        priority = "Normal"

    # Evidence (support multiple if stored as comma-separated paths)
    evidence = []
    if complaint.evidence_path:
        evidence = complaint.evidence_path.split(",")

    # Pass all data to template
    return render_template(
        'student/complaint_detail.html',
        complaint=complaint,
        student=student,
        teacher=teacher,
        priority=priority,
        history=history,
        evidence=evidence
    )

@bp.route('/feedback', methods=['GET', 'POST'])
@login_required
def feedback():
    # Fetch resolved complaints of current student
    complaints = Complaint.query.filter_by(student_id=current_user.id, status='Resolved').all()

    form = FeedbackForm()
    form.complaint_id.choices = [(c.id, f"#{c.id} - {c.title} ({c.status})") for c in complaints]

    # Fetch previous feedback
    feedbacks = Feedback.query.filter_by(student_id=current_user.id).order_by(Feedback.created_at.desc()).all()

    if form.validate_on_submit():
        flash("Form submitted successfully!", "success")
        return redirect(url_for('student.feedback'))

    return render_template(
        'student/feedback.html',
        form=form,
        complaints=complaints,
        feedbacks=feedbacks
    )