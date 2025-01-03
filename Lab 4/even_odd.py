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
