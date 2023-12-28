from app import User, app
with app.app_context():
    # Retrieve all users from the 'User' table
    users = User.query.all()

    # Do something with the data
    for user in users:
        print(user.id, user.username, user.email, user.password)