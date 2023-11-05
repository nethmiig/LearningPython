# notes.py - Simple notes application

import datetime

# In-memory data storage
users = {"user1": "password1", "user2": "password2"}
notes = {}  # Dictionary to store notes for each user


# Function to create a note
def create_note(username):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    subject = input("\nSUBJECT: ")
    note_text = input("NOTE: \n")
    note = {"date": date, "subject": subject, "note_text": note_text}
    if username in notes:
        notes[username].append(note)
    else:
        notes[username] = [note]
    print("\nNOTE SAVED!\n")


# Function to retrieve and display notes


def retrieve_notes(username):
    if username in notes:
        print("Your notes:")
        for idx, note in enumerate(notes[username]):
            print(f"{idx + 1}. Date: {note['date']} - Subject: {note['subject']}")

        choice = input("Enter the note number to view or 'q' to quit: ")
        if choice == "q":
            return
        try:
            choice = int(choice)
            if 1 <= choice <= len(notes[username]):
                selected_note = notes[username][choice - 1]
                print(f"Date: {selected_note['date']}")
                print(f"Subject: {selected_note['subject']}")
                print("Note Text: ", selected_note["note_text"])
                action = input("Do you want to delete this note? (y/n): ")
                if action.lower() == "y":
                    notes[username].pop(choice - 1)
                    print("\nNOTE DELETED \n")
        except ValueError:
            print("Invalid input. Please enter a valid note number.")
    else:
        print("No notes found for this user.")


# Main application loop
while True:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Login")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    username = input("\nUsername: ")
    password = input("Password: ")
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    if username in users and users[username] == password:
        print(f"Welcome, {username}!")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        while True:
            print("\nCHOICES\n")
            print("1. CREATE")
            print("2. RETRIEVE/DELETE")
            print("3. DELETE ALL")
            print("4. LOGOUT\n")

            choice = input("Enter your choice: ")

            if choice == "1":
                create_note(username)
            elif choice == "2":
                retrieve_notes(username)
            elif choice == "3":
                notes.pop(username, None)
                print("All notes deleted.")

            elif choice == "4":
                print("Logged out. Goodbye!")
            break
    else:
        print("Invalid credentials. Please try again.")
