def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def y(f_num):
    print("""+
-
*
/""")
    oper = input("pick an operation: ")
    n_num = float(input("What is the next number?: "))

    result = (operations[oper](f_num, n_num))
    print(f"{f_num} {oper} {n_num} = {result}")
    return result



operations = {"+":add, "-":sub, "*":mul, "/":div}



while True:

    from art import logo

    print(logo)

    f_num = float(input("What is the first number?: "))
    result = y(f_num)

    while True:
        flow = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if flow == "y":
            result = y(result)
        else:
            print("\n"*100)
            break
