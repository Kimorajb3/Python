uList=set()

with open('unique.txt', 'r') as secret:
    
    
    for sep in secret.readlines():
        c=sep.split()
        
        for word in c:
            uList.add(word)

print("The unique words are : ", uList)
