#------------------------------------------------------------------
 # Class: CIST 2742 Beginning Python Programming
 # Term: Fall 2022
 # Instructor: Jianmin Wang
 # Description: Solution to Lab 4.2 Add/Even Number Counter
 # Due: 2/21/2022
 # author Kimora Bailey
 # version 1.0
 #
 # By turning in this code, I Pledge:
 #  1. That I have completed the programming assignment independently.
 #  2. I have not copied the code from a student or any source.
 #  3. I have not given my code to any student.
 #
 #---------------------------------------------------------------------
import random

def is_even(number):
    
    if(number % 2 == 0):
        return True
    else:
        return False
    

def main():
    
    evenCount = 0
    oddCount = 0
    numbers = list()
    
    for i in range(100):
        
        number = random.randint(1, 100)
        
        numbers.append(number)
        
        if(is_even(number)):
            
            evenCount = evenCount + 1
        else:
            
            oddCount = oddCount + 1

  
    print("The numbers generated are: \n")
    for x in range(len(numbers)):
        print ((str)(numbers[x]), end = " ")
        
    
    print("\n\nCount of Even numbers: " + (str)(evenCount))
    print("Count of Odd numbers: " + (str)(oddCount))
main()
