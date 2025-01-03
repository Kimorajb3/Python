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
