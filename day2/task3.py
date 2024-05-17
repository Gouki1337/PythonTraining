import sys
import getopt

def isPallindrom(input):
    retVal = None
    text = input.lower()
    text = text.replace(" ", "")
    strLen = len(text)

    if(strLen%2 == 0):
        for idx in range(0,int(strLen/2)):
            if (text[idx] != text[strLen-1-idx]):
                retVal = False
                break
            else:
                retVal = True          
    else:
        retVal = False
   
    return retVal


if __name__ == '__main__':
    argv = sys.argv[1:]
    input = None

    try:
        options, args = getopt.getopt(argv, "t:")
    except Exception as e:
        print(f"Error message! {e}")

for arg, value in options:
    if arg in ["-t"]:
        input = str(value)

print("Entered text:", input)

if (isPallindrom(input)):
    print(input, "is a pallindrom")
else:
    print(input, "is not a pallindrom")

