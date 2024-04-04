#------------------------------------------------------------------
 # Class: CIST 2742 Beginning Python Programming
 # Term: Fall 2022
 # Instructor: Jianmin Wang
 # Description: Solution to Lab 4.1 Refactor Calculator
 # Due: 2/21/2022
 # author Kimora Bailey
 # version 1.0
 #
 # By turning in this code, I Pledge:
 #  1. That I have completed the programming assignment independently.
 #  2. I have not copied the code from a student or any source.
 #  3. I have not given my code to any student.
 #
 #---------------------------------------------------------------------
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
