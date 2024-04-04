#------------------------------------------------------------------
# Class: CIST 2742 Beginning Python Programming
# Term: Fall 2022
# Instructor: Jianmin Wang
# Description: Solution to Lab 9.1 Employee Class
# Due: 4/11/2022
# author Kimora Bailey
# version 1.0
#
# By turning in this code, I Pledge:
#  1. That I have completed the programming assignment independently.
#  2. I have not copied the code from a student or any source.
#  3. I have not given my code to any student.
#
#---------------------------------------------------------------------
from employee import Employee

def main():
    E1 = Employee('Susan Meyers', '87899', 'Accounting', 'Vice President')
    E2 = Employee('Mark Jones', '39119', 'IT', 'Programmer')
    E3 = Employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer')
    print('Employee 1:')
    print(E1)
    print()
    print('Employee 2:')
    print(E2)
    print()
    print('Employee 3:')
    print(E3)

main()
