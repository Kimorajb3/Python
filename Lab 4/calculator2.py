def add(n1,n2):
    return n1+n2
def subtraction(n1,n2):
    return n1-n2
def multiplication(n1, n2):
    return n1*n2
def division(n1,n2):
    return n1/n2
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
ch = int(input("1 Addition\n2 Subtraction\n3 Multiplication\n4 Division\n"))
res = 0
if ch == 1:
    res = add(n1,n2)
elif ch == 2:
    res = subtraction(n1,n2)
elif ch == 3:
    res = multiplication(n1,n2)
elif ch == 4:
    res = division(n1,n2)
print(res)
