sent=[]
W=0
tf=open("text.txt",'r')   
for line in tf:
    sent.append(line)
    W+=len(line.split())
print("Total words are ",W) 
print("Average words in a sentence is ", W/len(sent)) 
Wmaximum=0 
Wminimum=len(sent[0].split()) 
Iminimum=0 
Imaximum=0
for i in range(len(sent)): 
    l=len(sent[i].split()) 
if l>Wmaximum: 
    Wmaximum=l
    Imaximum=i
if l<Wminimum: 
    Wminimum=l
    Iminimum=i
print("Max words in a sentence is:",sent[Imaximum])
print("It has ",Wmaximum," words.") 
print("Min words in a sentence is:",sent[Iminimum])
print("It has ",Wminimum," words.") 
