from flask import Blueprint, render_template, redirect, url_for, flash, request

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')
