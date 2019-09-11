def cholesterol_check():
    print("Cholesterol Check")
    chol = input("Enter your cholesterol result: ")
    chol_data = chol.split("=")
    if chol_data[0] == "HDL":
        result = check_HDL(chol_data[1])
        print("The cholesterol level is {}.".format(result))
