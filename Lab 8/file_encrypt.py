#------------------------------------------------------------------
 # Class: CIST 2742 Beginning Python Programming
 # Term: Fall 2022
 # Instructor: Jianmin Wang
 # Description: Solution to Lab 8.1 File Encryption
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
def en(codes):
    File = open('C:\\Users\\bellk\\OneDrive\\Documents\\Lab 8\\data.txt.txt', 'r')
    Read = File.read()

    ef = open('C:\\Users\\bellk\\OneDrive\\Documents\\Lab 8\\data2.txt.txt', 'w')

    for C in Read:
        if C in codes:
            ef.write(codes[C])
        else:
            ef.write(C)

    ef.close()

def de(codes):
    ef = open('C:\\Users\\bellk\\OneDrive\\Documents\\Lab 8\\data2.txt.txt', 'r')
    efRead = ef.read()

    for C in efRead:
        if not C in codes.values() or C == '.' or C == ' ':
            print(C, end='')
        else:
            for b, l in codes.items():
                if C == l:
                    print(b, end='')

def main():
    codes = {'A':'%', 'a':'9', 'B':'@', 'b':'#', 'C':'!', 'c':'1', 'D':'2', 'd':'5', \
             'E':'$', 'e':'4', 'F':'6', 'f':'^', 'G':'7', 'g':'&', 'H':'8', 'h':'*', 'I':'9', 'i':'(', \
             'J':')', 'j':'-', 'K':'+', 'k':'W', 'L':'f', 'l':'~', 'M':'l', 'm':'d', 'N':':', \
             'n':'P', 'O':'s', 'o':'q', 'Q':'>', 'q':'<', 'R':';', 'r':'j', 'S':'z', \
             's':'[','T':']', 't':'{', 'U':'}', 'u':'?', 'V':'/', 'v':'-', 'W':'_', 'w':'=', \
             'X':'r', 'x':'g', 'Y':'l', 'y':'S', 'Z':'u', 'z':'q'}
    en(codes)
    de(codes)

main()
