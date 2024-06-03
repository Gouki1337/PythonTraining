import string

def isPangram(input):
    alphabet = list(string.ascii_lowercase)

    for char in alphabet:
        if char not in input.lower():
            return False

    return True

def main():
    txt1 = "this is a test string"
    txt2 = "a quick brown fox jumps over the lazy dog"

    print("Text1:", isPangram(txt1))
    print("Text2:", isPangram(txt2))
    

if __name__ == '__main__': 
    main()