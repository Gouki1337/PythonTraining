if __name__ == "__main__":
    var1 = 10
    var2 = 20

    print("Var1:", var1, "Var2:", var2)

    var1, var2 = var2, var1
    print("Var1:", var1, "Var2:", var2)