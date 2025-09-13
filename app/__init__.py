from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# db = SQLAlchemy()
# login_manager = LoginManager()
# migrate = Migrate()

# Load .env variables
load_dotenv()

def create_app():
    app = Flask(__name__)

    # Load config from .env
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback_secret')
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///complaints.db')
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    # db.init_app(app)
    # login_manager.init_app(app)
    # migrate.init_app(app, db)

    # login_manager.login_view = 'auth.login'
    # login_manager.login_message_category = 'info'

    # Register blueprints
    # from app.routes.auth import bp as auth_bp
    from app.routes.student import bp as student_bp
    # from app.routes.admin import bp as admin_bp
    # from app.routes.teacher import bp as teacher_bp

    # app.register_blueprint(auth_bp)
    app.register_blueprint(student_bp)
    # app.register_blueprint(admin_bp)
    # app.register_blueprint(teacher_bp)

    return app
