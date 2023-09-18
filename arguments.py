#notes.py- Simple notes application

#modules
import sys

#main function
def main() -> int:
    
    print(sys.argv)
    print(sys.argv[1]+ print(sys.argv[2]))
   
    #casting to int
    a= int(sys.argv[1])
    b= int(sys.argv[2])
    #personal requests needs to be added here
    password=input("Password: ")
    print (a+b)
    print(a**b)
    

#return value
    return(0)
#main function definition
if __name__ == '__main__':
    sys.exit(main())