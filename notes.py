#notes.py- Simple notes application

#modules
import sys

#main function
def main() -> int:
    #Arguements 
    print(sys.argv)
    print(sys.argv[0])
    print(sys.argv[1])
    print(sys.argv[2])

    print(sys.argv[1]+sys.argv[2])
    print(23+32)
    a=int(sys.argv[1])
    b=int(sys.argv[2])
    print(a+b)
#return value
    return(0)
#main function definition
if __name__ == '__main__':
    sys.exit(main())