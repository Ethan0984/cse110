print()
grade = float(input('Enter your grade:'))
sign = ""
last_digit = grade % 10
if last_digit >= 7:
    sign = "+"
elif last_digit < 3:
    sign = "-"
else:
    sign = ""
if grade >= 93:
    sign = ""
if grade >= 90:
    print(f'Your grade is an A{sign}, you are passing the class.')
elif grade >= 80:
    print(f'Your grade is a B{sign}, you are passing the class.')
elif grade  >= 70:
    print(f'Your grade is a C{sign}, you are passing the class.')
elif grade >= 60:
    print(f'Your grade is a D{sign}, better luck next time.')
else:
    print('Your grade is an F, better luck next time.')