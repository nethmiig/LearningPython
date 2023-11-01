# notes.py - Simple notes application

# modules
import sys
import datetime

# ---- HARDCODED DATA STARTS HERE ----
# Usually we would use database but here lists are used to store users
users = ["user1", "user2", "user3"]
passwords = ["pass1", "pass2", "pass3"]

# notes is a list of note dictionary
notes = []

# First test note for first user
note = {
    "userid" : 0,
    "subject" : "sub1",
    "date" : datetime.datetime.now(),
    "text" : "text1"
}

# Add note to the notes list
notes.append(note)

# Second test note for second user
note = {
    "userid" : 1,
    "subject" : "sub2",
    "date" : datetime.datetime.now(),
    "text" : "text2"
}

# Add note to the notes list
notes.append(note)

# Third test note for first user
note = {
    "userid" : 0,
    "subject" : "sub3",
    "date" : datetime.datetime.now(),
    "text" : "text3"
}

# Add note to the notes list
notes.append(note)

# ---- HARDCODED DATA ENDS HERE ----

# authentication function
# returns : userid as an integer
# return value -1 means that user was not found
def authenticate(username, password) -> int:
    # Userid is used after the login to identify user
    userid = 0

    # Loop to authenticate user
    for u in users:
        # TODO: test prints
        # print(u)
        if u == username:
            if password != passwords[userid]:
                return -1
            else:
                return userid
        userid += 1

    # User was not found.
    return -1

# main function
def main() -> int:
    # Main loop that will run "forever" - TODO: add exit later
    while (True):
        # userid is set initially to -1. In this app it means that user is not authenticated.
        userid = -1

        # Login loop
        while (userid == -1):
            print("Login please:")
            username = input("Username: ")
            password = input("Password: ")
            userid = authenticate(username, password)

        # Empty line
        print()

        # Application logic starts here after successful authentication
        # TODO: add main menu
        # TODO: add notes menu



        # TODO: test print
        # print(notes)

        # Print notes for the user that has logged in
        print("Notes:")
        for n in notes:
            if n["userid"] == userid:
                print(n)

    # Exit successfully
    return(0)

# main function entry point
if __name__ == '__main__':
    sys.exit(main())