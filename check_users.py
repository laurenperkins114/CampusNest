from app import app, db, User  # Import the app object

# Create an application context to access the database
with app.app_context():
    users = User.query.all()  # Fetch all users from the database
    for user in users:
        print(f"Username: {user.username}, Password: {user.password}")
