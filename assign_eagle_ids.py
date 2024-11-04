from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/lperk/OneDrive/Desktop/HCI/CampusNest/instance/site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eagle_id = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    pronouns = db.Column(db.String(50), nullable=True)
    school = db.Column(db.String(150), nullable=True)
    security_question = db.Column(db.String(200), nullable=True)
    security_answer = db.Column(db.String(200), nullable=True)
    preferred_name = db.Column(db.String(150), nullable=True)
    classification = db.Column(db.String(50), nullable=True)
    major = db.Column(db.String(150), nullable=True)
    preferred_contact = db.Column(db.String(20), nullable=True)

def assign_eagle_id(username, eagle_id):
    user = User.query.filter_by(username=username).first()
    if user:
        user.eagle_id = eagle_id
        db.session.commit()
        print(f"Eagle ID '{eagle_id}' assigned to user '{username}' successfully.")
    else:
        print(f"User '{username}' not found.")

if __name__ == '__main__':
    with app.app_context():
        username = input("Enter the username of the user to assign an Eagle ID: ")
        eagle_id = input("Enter the Eagle ID to assign: ")
        assign_eagle_id(username, eagle_id)
