mealPrice = float(input('Enter charge of meal: $'))

tipAmount = .18
taxAmount = .07

tip = (mealPrice * tipAmount)
tax = (mealPrice * taxAmount)
total = mealPrice + tip + tax

print('\nCharge for food = $', format(mealPrice, ',.2f'), sep='')
print('Tip = $', format(tip, ',.2f'), sep='')
print('Sales tax = $', format(tax, ',.2f'), sep='')
print('Grand total = $', format(total, ',.2f'), sep='', end='\n\n')
