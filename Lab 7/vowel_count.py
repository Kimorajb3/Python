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
