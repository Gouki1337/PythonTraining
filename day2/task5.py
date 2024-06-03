if __name__ == '__main__':
    txt = ("Alfred", "Oskar", "Ludwig", "Mike")
    result = ""
    print("Text list:", txt)

    for idx in range(0, len(txt)):
        result += txt[idx]
        result += " "

    print("Result string:", result)
