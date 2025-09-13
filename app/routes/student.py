from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
# from app.models import Complaint
# from app import db

bp = Blueprint('student', __name__, url_prefix='/student')

@bp.route('/')
def home():
    return "<h1>My App</h1>"


