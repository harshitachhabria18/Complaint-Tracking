from flask import render_template, redirect, url_for, flash, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User, Teacher
from app.forms import RegistrationForm, LoginForm

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/register", methods=["GET","POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        # check if email already exists
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash("An account with this email already exists.", "danger")
            return redirect(url_for("auth.register"))
        
     # create user
        new_user = User(
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            department=form.department.data,
            role=form.role.data,
            password_hash=generate_password_hash(form.password.data)
        )
        db.session.add(new_user)
        db.session.flush()  # get new_user.id before commit

        # if teacher, create teacher profile
        if form.role.data == "teacher":
            teacher = Teacher(
                id=new_user.id,
                category=form.category.data  # from form
            )
            db.session.add(teacher)

        db.session.commit()

         # log in new user immediately if you want
        login_user(new_user)
        flash("Your account has been created successfully!", "success")
        return redirect(url_for("auth.login"))  # or dashboard

    return render_template("auth/register.html", form=form)

@bp.route("/login", methods=["GET", "POST"])
def login():
    # if current_user.is_authenticated:
    #     return "<h1>Hello World</h1>"  # redirect to dashboard if already logged in

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash("Logged in successfully!", "success")
            return redirect(url_for("student.home"))
            # next_page = request.args.get("next")
            # return "<h1>Hello World</h1>"
        else:
            flash("Invalid email or password.", "danger")

    return render_template("auth/login.html", form=form)

@bp.route("/logout")
@login_required 
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.login"))
