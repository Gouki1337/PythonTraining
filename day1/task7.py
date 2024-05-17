import sys
import getopt

if __name__ == '__main__':
    argv = sys.argv[1:]
    input = None

    try:
        options, args = getopt.getopt(argv, "d:")
    except Exception as e:
        print(f"Error message! {e}")

for arg, value in options:
    if arg in ["-d"]:
        input = int(value)

print("Number of days entered:", input)

days = 0
weeks = 0
years = 0

if (input >= 7):
    weeks = int(input / 7)
    days = int(input % 7)

if (weeks >= 52):
    years = int(weeks / 52)
    weeks = int(weeks % 52)
    
print("Result:", days, "days,", weeks, "weeks,", years, "years")