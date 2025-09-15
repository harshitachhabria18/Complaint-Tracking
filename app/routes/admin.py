from flask import Blueprint, render_template, redirect, url_for, flash, request

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/')
def dashboard():
    return render_template('admin/dashboard.html')

@bp.route('/complaints')
def complaints():
    return render_template('admin/complaints.html')

@bp.route('/analytics')
def analytics():
    return render_template('admin/analytics.html')