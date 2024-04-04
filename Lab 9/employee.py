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
class Employee():

    def __init__(self,name,ID,dept,JT):
        self.name=name
        self.id=ID
        self.department=dept
        self.jt=JT


    def setname(self,name):
        self.name=name
    def setID(self,ID):
        self.id=ID
    def setdept(self,dept):
        self.department=dept
    def setJT(self,JT):
        self.jt = JT

    def __str__(self):
        return "Name: %s, ID: %s, Department: %s, Job Title: %s"%(self.name,self.id,self.department,self.jt)
