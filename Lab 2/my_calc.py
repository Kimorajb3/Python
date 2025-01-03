title = "My Calculator"
Input = "x"
while (Input == 'x'):
    n1 = int(input("Enter Number 1: "))
    n2 = int(input("Enter Number 2: "))
    print("Please select operation to be performed:\nadd\nsubtract\nmultiply\ndivide")
    op = input("Your choice:  ")
    if op == 'add':
        result = n1 + n2
    elif op == 'subtract':
        result = n1 - n2
    elif op == 'multiply':
        result = n1 * n2
    elif op == 'divide':
        result = n1 / n2
    else:
        print("You didn't enter a valid operator")
    print(title)
    print("\n")
    print("The {} of {} and {} is {}, where {} is the operation entered, {} and {} are the numbers entered and {} is the result of the operation".format(op, n1, n2, result, op, n1, n2, result))
print("Thanks for using the calculator")
