#------------------------------------------------------------------
 # Class: CIST 2742 Beginning Python Programming
 # Term: Fall 2022
 # Instructor: Jianmin Wang
 # Description: Solution to Lab 1.4 calculate tip, tax, and sales total
 # Due: 1/31/2022
 # author Kimora Bailey
 # version 1.0
 #
 # By turning in this code, I Pledge:
 #  1. That I have completed the programming assignment independently.
 #  2. I have not copied the code from a student or any source.
 #  3. I have not given my code to any student.
 #
 #---------------------------------------------------------------------
mealPrice = float(input('Enter charge of meal: $'))

tipAmount = .18
taxAmount = .07

tip = (mealPrice * tipAmount)
tax = (mealPrice * taxAmount)
total = mealPrice + tip + tax

print('\nCharge for food = $', format(mealPrice, ',.2f'), sep='')
print('Tip = $', format(tip, ',.2f'), sep='')
print('Sales tax = $', format(tax, ',.2f'), sep='')
print('Grand total = $', format(total, ',.2f'), sep='', end='\n\n')
