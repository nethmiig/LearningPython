# notes.py - Simple notes application
# In-memory data storage
users = {"user1": "password1", "user2": "password2"}
notes = {}  # Dictionary to store notes for each user


# Function to create a note
def create_note(username):
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in users and users[username] == password:
            print(f"Welcome, {username}!")
            while True:
                print("\nOptions:")
                print("1. Create Note")
                print("2. Retrieve or Read Notes")
                print("3. Delete Notes")
                print("4. Logout")
                choice = input("Enter your choice: ")
    else:
        print("Invalid credentials. Please try again.")
