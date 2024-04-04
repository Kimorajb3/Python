#------------------------------------------------------------------
 # Class: CIST 2742 Beginning Python Programming
 # Term: Fall 2022
 # Instructor: Jianmin Wang
 # Description: Solution to Lab 2.2 calculator
 # Due: 2/07/2022
 # author Kimora Bailey
 # version 1.0
 #
 # By turning in this code, I Pledge:
 #  1. That I have completed the programming assignment independently.
 #  2. I have not copied the code from a student or any source.
 #  3. I have not given my code to any student.
 #
 #---------------------------------------------------------------------
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
