def isPrime(number):
    for i in range(2,number):
        if (number%i) == 0:
            return False
    return True


def main():
    input = 1432  
    print("Number:", input, "- Prime:", isPrime(input))

if __name__ == '__main__': 
    main()