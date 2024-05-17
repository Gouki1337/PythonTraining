import sys
import getopt

if __name__ == "__main__":
    argv = sys.argv[1:]
    input = None

    try:
        options, args = getopt.getopt(argv, "s:")
    except Exception as e:
        print(f"Error message! {e}")

    for arg, value in options:
        if arg in ["-s"]:
            sentence = value
            
    numOfWords = len(sentence.split())
    print("Input sentence:", sentence)
    print("Counted words in senctence:", numOfWords)
