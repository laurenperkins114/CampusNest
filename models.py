# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
