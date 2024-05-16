import sys

if __name__ == '__main__':
    if len(sys.argv) <= 2:
        print("Invalid number of arguments. Script will be terminated.")
    else:
        name = str(sys.argv[1])
        age = str(sys.argv[2])
        print("Welcome",name,". Your age is",age,".")
    