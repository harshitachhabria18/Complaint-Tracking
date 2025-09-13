from app import create_app
from flask_migrate import upgrade

app = create_app()

# with app.app_context():
#     db.create_all()  # creates all tables if they don’t exist

if __name__ == "__main__":
    app.run(debug=True)
