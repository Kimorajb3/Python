#------------------------------------------------------------------
 # Class: CIST 2742 Beginning Python Programming
 # Term: Fall 2022
 # Instructor: Jianmin Wang
 # Description: Solution to Lab 3.2 Sum of Numbers
 # Due: 2/14/2022
 # author Kimora Bailey
 # version 1.0
 #
 # By turning in this code, I Pledge:
 #  1. That I have completed the programming assignment independently.
 #  2. I have not copied the code from a student or any source.
 #  3. I have not given my code to any student.
 #
 #---------------------------------------------------------------------
total = 0
num = float(input("Enter a positive number(negative exits program): "))

while num >= 0:
    total += num
    num = (float(input("Enter a positive number(negative exits program): ")))
    print("Sum:", total)
