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
#importing Person class
from person import Person

class Student(Person):
    #assign values and passing data
    def __init__(self, first_name="", last_name="", address="", city="", zip="", graduation_year = 0, major = ""):
        super().__init__(first_name, last_name, address, city, zip)
        self.graduation_year = graduation_year
        self.major = major

    #creating accessor and mutator methods
    def getgradyr(self):
        return self.graduation_year

    def getmaj(self):
        return self.major

    def setgardyr(self, graduation_year):
        self.graduation_year = graduation_year

    def setmaj(self, major):
        self.major = major

    #graduation year and major method
    def gradinfo(self):
        return print('Graduation year: {}, Major: {}'.format(self.getgradyr(), self.getmaj()))

    #greeting method
    def greeting(self):
        return print('Welcome {} {} to the class of {}'.format(self.getfn(), self.getln(),self.getgradyr()))
