from app import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__ = 'users'  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255),nullable=False)
    role = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    department = db.Column(db.String(50), nullable=False) # B.Tech/BCA/etc
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # One-to-one relationship to teacher profile (if role = teacher)
    teacher_profile = db.relationship('Teacher', backref='user', uselist=False)

class Teacher(db.Model):
    __tablename__ = 'teachers'  
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    category = db.Column(db.String(100), nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)

# class Complaint(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     student_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     category = db.Column(db.String(100))
#     title = db.Column(db.String(200))
#     description = db.Column(db.Text)
#     evidence_path = db.Column(db.String(255))
#     anonymous = db.Column(db.Boolean, default=False)
#     status = db.Column(db.Enum('Pending','In Progress','Resolved','Escalated', name='status_enum'), default='Pending')
#     severity = db.Column(db.Enum('Normal','Urgent','Critical', name='severity_enum'), default='Normal')
#     assigned_teacher_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     deadline = db.Column(db.DateTime)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# class ComplaintHistory(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     complaint_id = db.Column(db.Integer, db.ForeignKey('complaint.id'))
#     status = db.Column(
#     db.Enum('Pending', 'In Progress', 'Resolved', 'Escalated', name='history_status_enum'))
#     remarks = db.Column(db.Text)
#     evidence_path = db.Column(db.String(255))

# class Feedback(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     complaint_id = db.Column(db.Integer, db.ForeignKey('complaint.id'))
#     student_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     rating = db.Column(db.Integer)
#     comments = db.Column(db.Text)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)

# class Notification(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     message = db.Column(db.Text)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
