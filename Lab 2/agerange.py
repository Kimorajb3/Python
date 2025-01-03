age = int(input("Enter age: "))

if age < 20 or age >= 50:
    print("Your age is out of range")

elif age >= 20 and age < 30:
    print("Your are in your 20s")

elif age >= 30 and age < 40:
    print("Your are in your 30s")

elif age >= 40 and age < 50:
    print("Your are in your 40s")

else:
    print("Enter correct age")
