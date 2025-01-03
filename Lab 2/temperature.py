title = "Temperature Conversion Application"
print(title)

tempCon = str(input('Type F for Fahrenheit to Centigrade or C for Centigrade to Fahrenheit: '))

tempDeg = float(input('Enter temperature: '))

if tempCon == 'F':
    celsius = 5/9*(tempDeg-32)
    print('%.2f Fahrenheit is: %0.2f Celsius' %(tempDeg, celsius))
elif tempCon == 'C':
    fahrenheit = 9/5*tempDeg+32
    print('%.2f Celsius is: %0.2f Fahrenheit' %(tempDeg, fahrenheit))
else:
    print('Enter correct value')
