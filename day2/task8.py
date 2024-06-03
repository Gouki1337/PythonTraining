def main():
    input = 120
    hours = 0
    minutes = 0

    hours = int(input/60)
    minutes = int(input%60)

    print("Input:", input, "minutes")
    print("Converted - Hours:", hours, "Minutes:", minutes)

if __name__ == '__main__': 
    main()