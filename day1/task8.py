if __name__ == '__main__':
    numberList = [1, 2, -1, -2, 3, -3, 4, -4, 5, -5] # sum: 15
    sum = 0

    print("Numbers:",numberList)

    for idx in range(0,len(numberList)):
        if (numberList[idx] >= 0):
            sum = sum + numberList[idx]
    
    print("Positive Quersumme:", sum)
