#notes.py- Simple notes application

#modules
import sys

#main function
def main() -> int:
    #login screen
    print("")
    username= input("Username: ")

    #personal requests needs to be added here
    password=input("Password: ")
    print(username,password)
    #notes screen
    print("1. some text")
    print("2. ...")
    input("Selection: ")

#return value
    return(0)
#main function definition
if __name__ == '__main__':
    sys.exit(main())