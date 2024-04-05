#------------------------------------------------------------------
# Class: CIST 2742 Beginning Python Programming
# Term: Fall 2022
# Instructor: Jianmin Wang
# Description: Solution to Lab 10 Inheritance
# Due: 4/18/2022
# author Kimora Bailey
# version 1.0
#
# By turning in this code, I Pledge:
#  1. That I have completed the programming assignment independently.
#  2. I have not copied the code from a student or any source.
#  3. I have not given my code to any student.
#
#---------------------------------------------------------------------
#importing student and person class
from student import Student
from person import Person

#Person object
Pers = Person('Steven', 'Christopher', 'Rainbow Rd', 'Galaxy', '20374')

#print full name and address
Pers.get_full_name()
Pers.get_full_address()

#Student object
Stu = Student('Pete', 'Cat', 'Fier St', 'Pennysworth', '56932', 2022, 'Accounting')

#print Student full name, gradinfo, and greet them
Stu.get_full_name()
Stu.gradinfo()
Stu.greeting()
