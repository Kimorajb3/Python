#------------------------------------------------------------------
 # Class: CIST 2742 Beginning Python Programming
 # Term: Fall 2022
 # Instructor: Jianmin Wang
 # Description: Solution to Lab 3.1 Divisible by 5 and 6
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
print("Numbers divisble by 5 or 6 are: ")
for i in range(1,101):
    if i % 5 == 0 or i % 6 == 0:
        print(str(i), end=' ')
print("\n")

print("Numbers divisble by 5 and 6 are: ")
for i in range(1,101):
    if i % 5 == 0 and i % 6 == 0:
        print(str(i), end=' ')
