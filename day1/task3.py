import sys
import getopt

def isOdd(value):
    retVal = False

    if ((int(value) % 2) != 0):
        retVal = True

    return retVal

if __name__ == '__main__':
    argv = sys.argv[1:]
    num = None

    try:
        options, args = getopt.getopt(argv, "n:")
    except Exception as e:
        print(f"Error message! {e}")

for arg, value in options:
    if arg in ["-n"]:
        num = value

print("Entered number is: " + num)

if (isOdd(num)):
    print("Number is odd.")
else:
    print("Number is even.")    
