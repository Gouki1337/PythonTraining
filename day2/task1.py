if __name__ == '__main__':
    
    numList = list(range(1,11)) #55
    summe = 0
    average= 0

    print("Numbers:",numList)

    summe = sum(numList)
    average = sum(numList)/len(numList)

    print("Summe:", summe)
    print("Average:", average)
