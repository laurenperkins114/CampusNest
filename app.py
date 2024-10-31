from flask import Flask, render_template, redirect, url_for, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set a secret key for session management
app.secret_key = 'your_unique_secret_key'  # Change this to something more secure

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define your database models here
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

class Event(db.Model):
    __tablename__ = 'events'
    event_id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.String)
    day = db.Column(db.Integer)
    year = db.Column(db.Integer)
    time = db.Column(db.String)
    location = db.Column(db.String)
    details = db.Column(db.Text)

class Task(db.Model):
    __tablename__ = 'tasks'
    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.Text)
    dueDate = db.Column(db.Date)
    completed = db.Column(db.Boolean, default=False)
    rsvp = db.Column(db.Integer, default=0)

class Member(db.Model):
    __tablename__ = 'members'
    member_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)

class EventMember(db.Model):
    __tablename__ = 'event_members'
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'), primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('members.member_id'), primary_key=True)

class TaskMember(db.Model):
    __tablename__ = 'task_members'
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.task_id'), primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('members.member_id'), primary_key=True)

# Create the database
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
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['username'] = username  # Store username in session
            return redirect(url_for('home_page'))
        else:
            return "Invalid username or password", 401
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
@app.route('/signup.html')
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/user-profile')
@app.route('/user-profile.html')
def user_profile():
    username = session.get('username', 'Guest')  # Get username from session
    return render_template('user-profile.html', username=username)

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove username from session
    return redirect(url_for('login'))

# Route to get all events
@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([{
        'event_id': event.event_id,
        'month': event.month,
        'day': event.day,
        'year': event.year,
        'time': event.time,
        'location': event.location,
        'details': event.details
    } for event in events])


if __name__ == '__main__':
    app.run(debug=True)
