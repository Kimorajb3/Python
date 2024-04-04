#------------------------------------------------------------------
 # Class: CIST 2742 Beginning Python Programming
 # Term: Fall 2022
 # Instructor: Jianmin Wang
 # Description: Solution to Lab 2.1 convert temperature
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

title = "Temperature Conversion Application"
print(title)

tempCon = str(input('Type F for Fahrenheit to Centigrade or C for Centigrade to Fahrenheit: '))

tempDeg = float(input('Enter temperature: '))

if tempCon == 'F':
    celsius = 5/9*(tempDeg-32)
    print('%.2f Fahrenheit is: %0.2f Celsius' %(tempDeg, celsius))
elif tempCon == 'C':
    fahrenheit = 9/5*tempDeg+32
    print('%.2f Celsius is: %0.2f Fahrenheit' %(tempDeg, fahrenheit))
else:
    print('Enter correct value')
