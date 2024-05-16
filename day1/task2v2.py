import sys
import getopt

argName = ""
argAge = ""
argv = sys.argv[1:]

try:
    options, args = getopt.getopt(argv, "n:a:", ["name =", "age ="])
except Exception as e:  # noqa: E722
    print(f"Error message! {e}")
    

for arg, value in options:
    if arg in ['-n', '--name ']:
        argName = value
    elif arg in ['-a', '--age ']:
        argAge = value

print("Hello " + argName + ". You look beautiful in the age of " + argAge)
