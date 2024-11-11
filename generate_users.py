from sqlalchemy import create_engine, Column, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import random

# Define the database and ORM setup
Base = declarative_base()
engine = create_engine('sqlite:///instance/site.db')
Session = sessionmaker(bind=engine)
session = Session()

# Define the User model
class User(Base):
    __tablename__ = 'user'
    eagle_id = Column(String(150), primary_key=True)  # Make eagle_id the primary key
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    username = Column(String(150), nullable=False, unique=True)
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(150), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    phone_number = Column(String(20), nullable=True)
    pronouns = Column(String(50), nullable=True)
    school = Column(String(150), nullable=True)
    security_question = Column(String(200), nullable=True)
    security_answer = Column(String(200), nullable=True)
    preferred_name = Column(String(150), nullable=True)  # Ensure this line is present
    classification = Column(String(50), nullable=True)
    major = Column(String(150), nullable=True)
    preferred_contact = Column(String(20), nullable=True)  # Ensure this line is present

# Create the table if it doesn't exist
Base.metadata.create_all(engine)

# Example users including Gus and 10 more users
example_users = [
    {
        "eagle_id": "123456789",
        "first_name": "Gus",
        "last_name": "Eagle",
        "username": "GusTheEagle",
        "email": "gusTHEeagle@georgiasouthern.edu",
        "password": "gustheeagle",
        "date_of_birth": "1906-12-01",
        "phone_number": "1200101906",
        "pronouns": "him/his",
        "school": "Georgia Southern University",
        "security_question": "In which city were you born in?",
        "security_answer": "Statesboro",
        "preferred_name": "Gus Gus",
        "classification": "Higher Education",
        "major": "Computer Science",
        "preferred_contact": "Email"
    },
    {
        "eagle_id": "901456789",
        "first_name": "John",
        "last_name": "Doe",
        "username": "jdoe",
        "email": "john.doe@example.com",
        "password": "password123",
        "date_of_birth": "1990-01-01",
        "phone_number": "(123) 456-7890",
        "pronouns": "he/him",
        "school": "Example University",
        "security_question": "In which city were you born in?",
        "security_answer": "Atlanta",
        "preferred_name": "Johnny",
        "classification": "Sophomore",
        "major": "Computer Science",
        "preferred_contact": "email"
    },
    {
        "eagle_id": "901098765",
        "first_name": "Alice",
        "last_name": "Walker",
        "username": "awalker",
        "email": "alice.walker@example.com",
        "password": "securepass456",
        "date_of_birth": "1985-05-21",
        "phone_number": "(555) 123-4567",
        "pronouns": "she/her",
        "school": "Springfield College",
        "security_question": "Name of your favorite teacher?",
        "security_answer": "Mr. Johnson",
        "preferred_name": "Ally",
        "classification": "Junior",
        "major": "Biology",
        "preferred_contact": "phone"
    },
    {
        "eagle_id": "901345678",
        "first_name": "Robert",
        "last_name": "Miller",
        "username": "rmiller",
        "email": "robert.miller@example.com",
        "password": "password789",
        "date_of_birth": "1993-07-15",
        "phone_number": "(555) 234-5678",
        "pronouns": "he/him",
        "school": "Hillside University",
        "security_question": "Name of your favorite pet?",
        "security_answer": "Buddy",
        "preferred_name": "Rob",
        "classification": "Senior",
        "major": "Physics",
        "preferred_contact": "email"
    },
    {
        "eagle_id": "901234567",
        "first_name": "Emily",
        "last_name": "Garcia",
        "username": "egarcia",
        "email": "emily.garcia@example.com",
        "password": "mypassword123",
        "date_of_birth": "1996-09-10",
        "phone_number": "(555) 345-6789",
        "pronouns": "they/them",
        "school": "Greenfield University",
        "security_question": "Name of your favorite pet?",
        "security_answer": "Fluffy",
        "preferred_name": "Em",
        "classification": "Freshman",
        "major": "Engineering",
        "preferred_contact": "email"
    },
    {
        "eagle_id": "901567890",
        "first_name": "David",
        "last_name": "Wilson",
        "username": "dwilson",
        "email": "david.wilson@example.com",
        "password": "wilsonsecure1",
        "date_of_birth": "1988-03-30",
        "phone_number": "(555) 456-7890",
        "pronouns": "he/him",
        "school": "Lakeside College",
        "security_question": "Name of your favorite teacher?",
        "security_answer": "Mrs. Thompson",
        "preferred_name": "Dave",
        "classification": "Higher Ed",
        "major": "Business Administration",
        "preferred_contact": "phone"
    },
    {
        "eagle_id": "901678901",
        "first_name": "Sarah",
        "last_name": "Johnson",
        "username": "sjohnson",
        "email": "sarah.johnson@example.com",
        "password": "password123",
        "date_of_birth": "1994-02-14",
        "phone_number": "(555) 678-9012",
        "pronouns": "she/her",
        "school": "Blue Ridge University",
        "security_question": "Name of your favorite pet?",
        "security_answer": "Rex",
        "preferred_name": "Sally",
        "classification": "Sophomore",
        "major": "Economics",
        "preferred_contact": "phone"
    },
    {
        "eagle_id": "901789012",
        "first_name": "Michael",
        "last_name": "Anderson",
        "username": "manderson",
        "email": "michael.anderson@example.com",
        "password": "secure1234",
        "date_of_birth": "1990-06-22",
        "phone_number": "(555) 789-0123",
        "pronouns": "he/him",
        "school": "University of Oak Ridge",
        "security_question": "Name of your favorite pet?",
        "security_answer": "Buster",
        "preferred_name": "Mike",
        "classification": "Junior",
        "major": "Mathematics",
        "preferred_contact": "email"
    },
    {
        "eagle_id": "901890123",
        "first_name": "Samantha",
        "last_name": "Taylor",
        "username": "staylor",
        "email": "samantha.taylor@example.com",
        "password": "samsecure1",
        "date_of_birth": "1995-08-25",
        "phone_number": "(555) 890-1234",
        "pronouns": "she/her",
        "school": "Lakeview College",
        "security_question": "Name of your favorite pet?",
        "security_answer": "Charlie",
        "preferred_name": "Sam",
        "classification": "Senior",
        "major": "Political Science",
        "preferred_contact": "phone"
    },
    {
        "eagle_id": "901901234",
        "first_name": "Joseph",
        "last_name": "White",
        "username": "jwhite",
        "email": "joseph.white@example.com",
        "password": "mypassword456",
        "date_of_birth": "1992-11-03",
        "phone_number": "(555) 901-2345",
        "pronouns": "he/him",
        "school": "Horizon University",
        "security_question": "Name of your favorite pet?",
        "security_answer": "Toby",
        "preferred_name": "Joe",
        "classification": "Higher Ed",
        "major": "Psychology",
        "preferred_contact": "email"
    },
    {
        "eagle_id": "901234890",
        "first_name": "Olivia",
        "last_name": "Davis",
        "username": "odavis",
        "email": "olivia.davis@example.com",
        "password": "password789",
        "date_of_birth": "1997-05-18",
        "phone_number": "(555) 234-8901",
        "pronouns": "she/her",
        "school": "Greenwood University",
        "security_question": "Name of your favorite pet?",
        "security_answer": "Bella",
        "preferred_name": "Liv",
        "classification": "Freshman",
        "major": "Environmental Science",
        "preferred_contact": "phone"
    },
    {
        "eagle_id": "901012345",
        "first_name": "Andrew",
        "last_name": "Morris",
        "username": "amorris",
        "email": "andrew.morris@example.com",
        "password": "andrew123",
        "date_of_birth": "1998-09-22",
        "phone_number": "(555) 123-4568",
        "pronouns": "he/him",
        "school": "Sunset University",
        "security_question": "Name of your favorite pet?",
        "security_answer": "Luna",
        "preferred_name": "Drew",
        "classification": "Sophomore",
        "major": "History",
        "preferred_contact": "email"
    },
    {
        "eagle_id": "902345678",
        "first_name": "Sophia",
        "last_name": "Martinez",
        "username": "smartinez",
        "email": "sophia.martinez@example.com",
        "password": "sophia456",
        "date_of_birth": "1993-02-17",
        "phone_number": "(555) 345-6789",
        "pronouns": "she/her",
        "school": "Pinewood College",
        "security_question": "Name of your favorite pet?",
        "security_answer": "Milo",
        "preferred_name": "Sophie",
        "classification": "Senior",
        "major": "Philosophy",
        "preferred_contact": "email"
    }
]

# Insert example users into the database
for user_data in example_users:
    user = User(
        eagle_id=user_data["eagle_id"],  # Use the custom eagle_id provided
        first_name=user_data["first_name"],
        last_name=user_data["last_name"],
        username=user_data["username"],
        email=user_data["email"],
        password=user_data["password"],
        date_of_birth=datetime.strptime(user_data["date_of_birth"], "%Y-%m-%d"),
        phone_number=user_data["phone_number"],
        pronouns=user_data["pronouns"],
        school=user_data["school"],
        security_question=user_data["security_question"],
        security_answer=user_data["security_answer"],
        preferred_name=user_data["preferred_name"],
        classification=user_data["classification"],
        major=user_data["major"],
        preferred_contact=user_data["preferred_contact"]
    )
    session.add(user)

session.commit()
print("Example users inserted into site.db.")
session.close()
