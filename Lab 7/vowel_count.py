#------------------------------------------------------------------
 # Class: CIST 2742 Beginning Python Programming
 # Term: Fall 2022
 # Instructor: Jianmin Wang
 # Description: Solution to Lab 7.3 Vowels and Consonants
 # Due: 3/21/2022
 # author Kimora Bailey
 # version 1.0
 #
 # By turning in this code, I Pledge:
 #  1. That I have completed the programming assignment independently.
 #  2. I have not copied the code from a student or any source.
 #  3. I have not given my code to any student.
 #
 #---------------------------------------------------------------------
def Vowels(STR): 
        ct = 0
        for i in range(len(STR)): 
                if(STR[i] in "aeiouAEIOU"): 
                        ct = ct + 1 
        return ct


def Consonants(STR): 
        ct = 0  
        for i in range(len(STR)):  
                if(STR[i] not in "aeiouAEIOU"): 
                        ct = ct + 1
        return ct
        
STR=input("Enter String: ")
print("Total Vowels: ",Vowels(STR))
print("Total Consonants: ",Consonants(STR))
