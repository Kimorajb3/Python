#------------------------------------------------------------------
 # Class: CIST 2742 Beginning Python Programming
 # Term: Fall 2022
 # Instructor: Jianmin Wang
 # Description: Solution to Lab 7.2 Character Statistics
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
def main():
    
    Upper = 0
    Lower = 0
    Spaces = 0
    Digits = 0
    DA = ''
    
    tf = open('text.txt', 'r')
    
    DA = tf.read()
    
    for ch in DA:
        if ch.isupper():
            Upper = Upper + 1
        if ch.islower():
            Lower = Lower + 1
        if ch.isdigit():
            Digits = Digits + 1
        if ch.isspace():
            Spaces = Spaces + 1
    
    tf.close()
    
    print('Total Uppercase:', Upper)
    print('Total Lowercase:', Lower)
    print('Total Digits:', Digits)
    print('Total Spaces:', Spaces)


main()
