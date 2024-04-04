#------------------------------------------------------------------
 # Class: CIST 2742 Beginning Python Programming
 # Term: Fall 2022
 # Instructor: Jianmin Wang
 # Description: Solution to Lab 8.2 Unique Words
 # Due: 3/28/2022
 # author Kimora Bailey
 # version 1.0
 #
 # By turning in this code, I Pledge:
 #  1. That I have completed the programming assignment independently.
 #  2. I have not copied the code from a student or any source.
 #  3. I have not given my code to any student.
 #
 #---------------------------------------------------------------------
uList=set()

with open('unique.txt', 'r') as secret:
    
    
    for sep in secret.readlines():
        c=sep.split()
        
        for word in c:
            uList.add(word)

print("The unique words are : ", uList)
