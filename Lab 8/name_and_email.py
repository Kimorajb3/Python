import pickle
import sys

try:
    file=open('email.txt','rb')
    dictionary=pickle.load(file)
    file.close()
     
except:  
    dictionary={}

while True:

    print('1. Find a email address')
    print('2. Add name and email address')
    print('3. Change an email address')
    print('4. Delete an email address')
    print('5. Exit')

    C=input('Enter a choice: ')

    if C:
        C=int(C)
    else:
        print('Enter number')
        continue  

    if C == 1:

        while True:

            N=input('Enter name ')

            if N:
                if N in dictionary:
                    print('%s is the Email of %s ' % (dictionary[N],N))
                    break
                else:
                    print(' Not Found ')
                    break
            else:
                print('Please Enter Name')
                continue
          
    elif C==2:

        while True:          
      
            N=input('Enter name ')

            if N:
                break;
            else:
                print('Please Enter Name ')
                continue

        while True:          
      
            Em=input('Enter Email ')

            if Em:
                dictionary[N]=Em
                break
            else:
                print('Please Enter an Email')
                continue
          
    elif C==3:

        while True:          
      
            N=input('Enter name to change email ')

            if N:
                if N in dictionary:
                    Em=input('Enter new email address ')
                    dictionary[N]=Em
                    print('Email Changed Successfully ')
                    break;
                else:
                    print('Not Found ')
                    break
            else:
                print('Please Enter a Name ')
                continue
          
    elif C == 4:

        while True:          
      
            N=input('Enter name to delete ')

            if N:
                if N in dictionary:
                    del dictionary[N]
                    print('Name and Email removed ')
                    break;
                else:
                    print('Not found ')
                    break
            else:
                print('Please Enter a Name')
                continue

    elif C == 5:
      
        file=open('email.txt','wb')
        pickle.dump(dictionary,file)
        file.close()
        sys.exit()
    else:
        print('Enter correct response ')
