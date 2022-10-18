print()
first_age = int(input('What is the age of the first rider? '))
if first_age >= 18 :
    first_age_ride = True
else:
    first_age_ride = False
first_height = int(input('What is the height of the first rider? '))
if first_height < 36:
    first_height_ride = False
elif first_height >= 62:
    first_height_ride = True
else:
    first_height_ride = False
second = str(input('Is there a second rider (yes/no)? ')).lower()
if second == "no":
    if first_age_ride and first_height_ride:
        print('You can ride. Be safe and have fun!')
    else:
        print("Sorry, you can't ride")
elif second == "yes":
    second_age = int(input('What is the age of the second rider? '))
    if second_age >= 18:
        second_age_ride = True
    else:
        second_age_ride = False
    second_height = int(input('What is the height of the second rider? '))
    if second_height < 36:
        second_height_ride = False
    elif second_height >= 62:
        second_height_ride = True
    else:
        second_height_ride = False
    if first_age < 36 or second_age < 36:
        first_age_ride = False
        second_age_ride = False
    if first_age_ride or second_age_ride:
        print('You can ride. Be safe and have fun!')
    else:
        print("Sorry, you can't ride")
else:
    print("Answer must be Yes or No")