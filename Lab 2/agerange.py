#------------------------------------------------------------------
 # Class: CIST 2742 Beginning Python Programming
 # Term: Fall 2022
 # Instructor: Jianmin Wang
 # Description: Solution to Lab 2.3 age range
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
age = int(input("Enter age: "))

if age < 20 or age >= 50:
    print("Your age is out of range")

elif age >= 20 and age < 30:
    print("Your are in your 20s")

elif age >= 30 and age < 40:
    print("Your are in your 30s")

elif age >= 40 and age < 50:
    print("Your are in your 40s")

else:
    print("Enter correct age")
