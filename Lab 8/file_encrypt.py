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
