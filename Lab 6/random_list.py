import random

def sum_list(numbers):
  total = 0
  for n in numbers:
    total += n
  return total

def max_list(numbers):
  maximum = numbers[0]
  for n in numbers:
    if n > maximum:
      maximum = n
  return maximum

def find_list(numbers, value):
  for n in numbers:
    if n == value:
      return True
  return False

def count_even(numbers):
  count = 0
  for n in numbers:
    if n % 2 == 0:
      count += 1
  return count


random_numbers = []
for _ in range(50):
  n = random.randint(1, 100)
  random_numbers.append(n)

print(f"Sum = {sum_list(random_numbers)}")
print(f"Maximum value = {max_list(random_numbers)}")
print(f"34 in list? {find_list(random_numbers, 34)}")
print(f"Count of even numbers = {count_even(random_numbers)}")
print(f"Sum of first 10 elements = {sum_list(random_numbers[0:10])}")
print(f"Sum of last 10 elements = {sum_list(random_numbers[-10:])}")

if sum_list(random_numbers[0:10]) > sum_list(random_numbers[-10:]):
  print("The sum of first 10 elements is greater than the last 10 elements")
elif sum_list(random_numbers[0:10]) < sum_list(random_numbers[-10:]):
  print("The sum of last 10 elements is greater than the first 10 elements")
else:
  print("The sum of last 10 elements is equal to the first 10 elements")
