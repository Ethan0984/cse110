print()
first_number = float(input('What is the first number? '))
second_number = float(input('What is the second number? '))
if first_number > second_number:
    print('The first number is greater')
    print('The numbers are not equal')
    print('The second number is not greater')
elif second_number > first_number:
    print('The first number is not greater')
    print('The numbers are not equal')
    print('The second number is greater')
else:
    print('The numbers are equal')
print()
animal = str(input('What is your favorite animal? '))
if animal == 'pigeon':
    print('Pigeons are my favorite animal too!')
else:
    print(f'{animal} is not my favorite animal.')