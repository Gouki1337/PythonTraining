def countVowels(input):
    #vowels ("a", "e", "i", "o", "u")

    print("A:", input.count("a"))
    print("E:", input.count("e"))
    print("I:", input.count("i"))
    print("O:", input.count("o"))
    print("U:", input.count("u"))


def main():
    input = "This is a test string"
    countVowels(input)

if __name__ == '__main__': 
    main()