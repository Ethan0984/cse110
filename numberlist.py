import math
finish = bool
finish = True
numbers = []
while finish == True:
    num = int(input('Enter number: '))
    numbers.append(num)
    if num == 0:
        finish = False
        break
Sum = sum(numbers)
print(f"Sum: {Sum}")
average = Sum / (len(numbers) - 1)
print(f"Average: {average}")
greatest = max(numbers)
print(f"The largest number is: {greatest}")
smallest = 99999
for number in numbers:
    if number > 0 and number < smallest:
        smallest = number
print(f"The smallest positive number is: {smallest}")
numbers.sort()
print(numbers)