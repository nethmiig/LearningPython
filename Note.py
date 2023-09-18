import sys

def main() -> int:
    print("ADD/RETRIEVE/DELETE")
    print("Enter choice: ")  
    userinput = input()
    if userinput== "add":
        print("Enter your note here: ")
        addnote=input()
        addnote= print(sys.argv)
        print(sys.argv[1]+ sys.argv[2])

    return(0)
if __name__ == '__main__':
    sys.exit(main())