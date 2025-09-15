from flask import Blueprint, render_template, flash, redirect, url_for, request, current_app
from flask_login import login_required, current_user
from datetime import datetime
from werkzeug.utils import secure_filename
import os
from app.forms import UpdateComplaintForm
from app import db
from app.models import Complaint

bp = Blueprint("teacher", __name__, url_prefix="/teacher")

@bp.route("/dashboard")
@login_required
def dashboard():
    if current_user.role != "teacher":
        flash("Unauthorized access!", "danger")
        return redirect(url_for("auth.login"))

    # Query complaints assigned to current teacher
    complaints = Complaint.query.filter_by(assigned_teacher_id=current_user.id).all()
    recent_complaints = (
        Complaint.query.filter_by(assigned_teacher_id=current_user.id)
        .order_by(Complaint.updated_at.desc())
        .limit(5)
        .all()
    )

    forms = {c.id: UpdateComplaintForm() for c in recent_complaints}
    # Stats
    total = len(complaints)
    pending = Complaint.query.filter_by(
        assigned_teacher_id=current_user.id,
        status="Pending"
    ).count()

    in_progress = Complaint.query.filter_by(
        assigned_teacher_id=current_user.id,
        status="InProgress"
    ).count()

    # Overdue = deadline has passed AND not resolved
    overdue = Complaint.query.filter(
        Complaint.assigned_teacher_id == current_user.id,
        Complaint.deadline < datetime.utcnow(),
        Complaint.status != "Resolved"
    ).count()

    
    return render_template(
        "teacher/dashboard.html",
        total=total,
        pending=pending,
        in_progress=in_progress,
        overdue=overdue,current_user=current_user,
        r_complaints = recent_complaints,
        now=datetime.utcnow(),
        forms = forms
    )

@bp.route("/complaint/<int:complaint_id>/update", methods=["POST"])
@login_required
def update_complaint(complaint_id):
    form = UpdateComplaintForm()
    complaint = Complaint.query.get_or_404(complaint_id)

    # Get form data
    if form.validate_on_submit():
        # Update fields
        complaint.status = form.status.data
        complaint.updated_at = datetime.utcnow()

        # Handle file upload
        if form.evidence.data:
            file = form.evidence.data
            filename = secure_filename(file.filename)

            # Create folder if not exists
            upload_folder = os.path.join(current_app.root_path, "static", "uploads", "teacher_evidences")
            os.makedirs(upload_folder, exist_ok=True)

            # Save file
            file_path = os.path.join(upload_folder, filename)
            file.save(file_path)
            complaint.evidence_path = f"uploads/teacher_evidences/{filename}"
        db.session.commit()
        flash("complaint updated successfully","success")
        return redirect(url_for("teacher.dashboard"))
    else:
        # If form fails validation
        flash("Some problem occurred while updating","danger")
        return redirect(url_for("teacher.dashboard"))