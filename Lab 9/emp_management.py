#------------------------------------------------------------------
# Class: CIST 2742 Beginning Python Programming
# Term: Fall 2022
# Instructor: Jianmin Wang
# Description: Solution to Lab 9.2 Employee Management
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
import pickle
import sys
from employee import Employee


try:
    file=open('employee.txt','rb')
    dictionary=pickle.load(file)
    file.close()
     
except:  
    dictionary={}

while True:

    print('1. Find Employee')
    print('2. Add Employee')
    print('3. Change Employee Information')
    print('4. Delete Employee')
    print('5. Exit')

    C=input('Enter a choice: ')

    if C:
        C=int(C)
    else:
        print('Enter number')
        continue  

    if C == 1:

        while True:

            ID=int(input('Enter ID '))
            emp = dictionary.get(ID)

            if ID:
                if ID in dictionary:
                    print(emp)
                    break
                else:
                    print(' Not Found ')
                    break
            else:
                print('Please Enter ID')
                continue
          
    elif C==2:
        N=input('Enter name ')
        ID=int(input('Enter ID '))
        Dept=input('Enter Department ')
        jt = input('Enter Job Title ')
        
        emp = Employee(N, ID, Dept, jt)
        dictionary[ID] = emp
        print('Employee Added Successfully')

    elif C==3:

        while True:          
      
            ID=int(input('Enter ID to change information '))

            if ID:
                if ID in dictionary:
                    N=input('Enter new name ')
                    ID = int(input('Enter new ID '))
                    Dept = input('Enter New Department ')
                    JT = input('Enter New Job Title ')

                    emp = Employee(N, ID, Dept, JT)
                    dictionary[ID] = emp
                    print('Information Changed Successfully ')
                    break;
                else:
                    print('Not Found ')
                    break
            else:
                print('Please Enter ID ')
                continue
          
    elif C == 4:

        while True:          
      
            ID=int(input('Enter ID to delete '))

            if ID:
                if ID in dictionary:
                    del dictionary[ID]
                    print('Employee removed ')
                    break;
                else:
                    print('Not found ')
                    break
            else:
                print('Please Enter ID')
                continue

    elif C == 5:
      
        file=open("employee.txt","wb")
        pickle.dump(dictionary,file)
        file.close()
        sys.exit()
    else:
        print('Enter correct response ')

