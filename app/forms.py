from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, BooleanField, FileField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional
from flask_wtf.file import FileField, FileAllowed, MultipleFileField

class RegistrationForm(FlaskForm):
    name = StringField(
        'Full Name',
        validators=[DataRequired(), Length(min=2, max=150)]
    )
    email = StringField(
        'Email Address',
        validators=[DataRequired(), Email()]
    )
    phone = StringField(
        'Phone Number',
        validators=[DataRequired(), Length(min=10, max=15)]
    )
    department = SelectField(
        'Department',
        choices=[
            ('', 'Select Department'),
            ('B.Tech', 'B.Tech'),
            ('BCA', 'BCA'),
            ('MCA', 'MCA'),
            ('MBA', 'MBA'),
            ('BBA', 'BBA'),
            ('Other', 'Other')
        ],
        validators=[DataRequired()]
    )
    role = SelectField(
        'Role',
        choices=[
            ('', 'Select Role'),
            ('student', 'Student'),
            ('teacher', 'Staff/Teacher'),
            ('admin', 'Administrator')
        ],
        validators=[DataRequired()]
    )
    category = SelectField(
        'Specialization Category',
        choices=[
            ('', 'Select Category'),
            ('academic', 'Academic Issues'),
            ('infrastructure', 'Infrastructure'),
            ('administrative', 'Administrative'),
            ('hostel', 'Hostel Facilities'),
            ('technical', 'Technical Support'),
            ('other', 'Other')
        ],
        validators=[Optional()]  # only required if role=teacher
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=6)]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )
    submit = SubmitField('Create Account')

class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(), Email(), Length(max=150)],
        render_kw={"placeholder": "Enter your email address"},
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=6)],
        render_kw={"placeholder": "Enter your password"},
    )
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")

class ComplaintForm(FlaskForm):
    title = StringField(
        "Complaint Title",
        validators=[DataRequired(), Length(max=200)]
    )

    category = SelectField(
        "Category",
        choices=[
            ("", "Select a category"),
            ("infrastructure", "Infrastructure"),
            ("academic", "Academic"),
            ("administration", "Administration"),
            ("hostel", "Hostel Facilities"),
            ("library", "Library"),
            ("transport", "Transport"),
            ("other", "Other")
        ],
        validators=[DataRequired()]
    )

    description = TextAreaField(
        "Detailed Description",
        validators=[DataRequired()]
    )

    evidence = MultipleFileField(
        "Upload Evidence",
        validators=[FileAllowed(
            ["jpg", "jpeg", "png", "pdf", "doc", "docx", "mp3", "wav", "mp4", "avi"],
            "Allowed file types: images, docs, audio, video"
        )]
    )
    
    anonymous = BooleanField("Submit anonymously")

    urgent = BooleanField("Mark as urgent")

    updates_email = BooleanField("Receive email updates about this complaint")

    submit = SubmitField("Submit Complaint")


class FeedbackForm(FlaskForm):
    complaint_id = SelectField(
        'Select Complaint',
        coerce=int,
        validators=[DataRequired(message="Please select a complaint")]
    )
    rating = HiddenField(
        'Rating',
        validators=[DataRequired(message="Please provide a rating")]
    )
    comments = TextAreaField(
        'Comments',
        validators=[DataRequired(message="Please provide your comments"),
                    Length(max=1000, message="Comments cannot exceed 1000 characters")]
    )
    submit = SubmitField('Submit Feedback')

class UpdateComplaintForm(FlaskForm):
    status = SelectField(
        "Status", 
        choices=[("pending", "Pending"), ("inprogress", "InProgress"), ("resolved", "Resolved")], 
        validators=[DataRequired()]
    )
    evidence = FileField(
        "Evidence", 
        validators=[DataRequired(), 
            FileAllowed(["jpg", "png", "pdf", "docx"])
        ]
    )

