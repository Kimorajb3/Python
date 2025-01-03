print("Numbers divisble by 5 or 6 are: ")
for i in range(1,101):
    if i % 5 == 0 or i % 6 == 0:
        print(str(i), end=' ')
print("\n")

print("Numbers divisble by 5 and 6 are: ")
for i in range(1,101):
    if i % 5 == 0 and i % 6 == 0:
        print(str(i), end=' ')
