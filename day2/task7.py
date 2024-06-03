import math

def calcArea(radius):
    return (pow(radius,2)*math.pi)

def calcCircumverence(radius):
   return (2*radius*math.pi)

def main():
    radius = 5.0

    print("Area:", calcArea(radius))
    print("Circumverence:", calcCircumverence(radius))

if __name__ == '__main__': 
    main()