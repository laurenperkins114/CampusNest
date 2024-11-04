from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# App config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/lperk/OneDrive/Desktop/HCI/CampusNest/instance/site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_unique_secret_key_here'  # Change this to a random string
db = SQLAlchemy(app)

class User(db.Model):
    eagle_id = db.Column(db.String(150), primary_key=True)  # Make eagle_id the primary key
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
    preferred_name = db.Column(db.String(150), nullable=True)  # Ensure this line is present
    classification = db.Column(db.String(50), nullable=True)
    major = db.Column(db.String(150), nullable=True)
    preferred_contact = db.Column(db.String(20), nullable=True)  # Ensure this line is present

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}, Eagle ID: {self.eagle_id}>'

# Create the database if it doesn't exist
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/home')
@app.route('/home.html')
def home_page():
    username = session.get('username', 'Guest')  # Get username from session
    return render_template('home.html', username=username)

@app.route('/admin')
@app.route('/admin.html')
def admin():
    return render_template('admin.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()  # Trim whitespace
        password = request.form['password'].strip()  # Trim whitespace
        
        print(f"Logging in with Username: '{username}', Password: '{password}'")  # Debug output
        
        # Look for the user in the database
        user = User.query.filter_by(username=username).first()
        
        # Check if user exists and verify password
        if user and user.password == password:  # Adjust this if you're hashing passwords
            session['username'] = username  # Store username in session
            return redirect(url_for('home_page'))
        else:
            flash("Invalid username or password", 'error')  # Use flash for error message
            return redirect(url_for('login'))
    
    return render_template('login.html')

from datetime import datetime

@app.route('/signup', methods=['GET', 'POST'])
@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Collect form data
        eagle_id = request.form.get('eagleId')  # Get the eagle ID from the form
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        date_of_birth_str = request.form['dateOfBirth']  # Get the date as a string
        date_of_birth = datetime.strptime(date_of_birth_str, '%Y-%m-%d').date()  # Convert to date object
        phone_number = request.form['phoneNumber']
        pronouns = request.form['pronouns']
        school = request.form['school']
        security_question = request.form['securityQuestion']
        security_answer = request.form['securityAnswer']

        # Create the new user and add to the database
        new_user = User(
            eagle_id=eagle_id,
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
            date_of_birth=date_of_birth,  # Now it's a date object
            phone_number=phone_number,
            pronouns=pronouns,
            school=school,
            security_question=security_question,
            security_answer=security_answer
        )

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            error_message = f'Error occurred: {e}'
            return render_template('signup.html', error=error_message)

    return render_template('signup.html')



@app.route('/user-profile', methods=['GET', 'POST'])
@app.route('/user-profile.html', methods=['GET', 'POST'])
def user_profile():
    username = session.get('username')  # Get username from session
    if username:
        user = User.query.filter_by(username=username).first()
        
        if request.method == 'POST':
            # Ensure all form fields are captured and updated
            return redirect(url_for('user_profile'))  # Redirect after update

        return render_template('user-profile.html', user=user, username=username)
    
    return redirect(url_for('login'))

@app.route('/update-profile', methods=['POST'])
def update_profile():
    username = session.get('username')
    if username:
        user = User.query.filter_by(username=username).first()
        
        # Log form data received for debugging
        print("Form data received for update:", request.form)

        # Update user information with defaults if blank
        user.first_name = request.form.get('first_name', user.first_name)
        user.last_name = request.form.get('last_name', user.last_name)
        user.preferred_name = request.form.get('preferred_name', user.preferred_name)
        user.classification = request.form.get('classification', user.classification)
        user.major = request.form.get('major', user.major)
        user.phone_number = request.form.get('phone', user.phone_number)
        user.preferred_contact = request.form.get('preferred_contact', user.preferred_contact)

        db.session.commit()
        print(f"User {username} updated their profile successfully.")
        
        return redirect(url_for('user_profile'))
    
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove username from session
    print("User logged out. Current session:", session)  # Debugging line
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
