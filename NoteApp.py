# notes.py - Simple notes application

import datetime

# In-memory data storage
users = {"user1": "password1", "user2": "password2"}
notes = {}  # Dictionary to store notes for each user


# Function to create a note
def create_note(username):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    subject = input("Enter the subject: ")
    note_text = input("Enter the note text: ")
    note = {"date": date, "subject": subject, "note_text": note_text}
    if username in notes:
        notes[username].append(note)
    else:
        notes[username] = [note]
    print("Note created successfully!")


# Function to retrieve and display notes


def retrieve_notes(username):
    if username in notes:
        print("Your notes:")
        for idx, note in enumerate(notes[username]):
            print(f"{idx + 1}. Date: {note['date']} - Subject: {note['subject']}")

        choice = input("Enter the note number to view or 'q' to quit: ")
        if choice == "q":
            return


# Main application loop
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print(f"Welcome, {username}!")
        while True:
            print("\nOptions:")
            print("1. Create Note")
            print("2. Retrieve Notes")
            print("3. Delete Notes")
            print("4. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                create_note(username)
            elif choice == "2":
                retrieve_notes(username)

            elif choice == "4":
                print("Logged out. Goodbye!")
            break
    else:
        print("Invalid credentials. Please try again.")
