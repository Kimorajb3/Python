total = 0
num = float(input("Enter a positive number(negative exits program): "))

while num >= 0:
    total += num
    num = (float(input("Enter a positive number(negative exits program): ")))
    print("Sum:", total)
