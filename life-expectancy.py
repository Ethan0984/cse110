lowest = 999
highest = -1
place = ""
highplace = ""
age = int
oldage = int

maxlife = -1
minlife = 999
area = ""
higharea = ""
date = int
olddate = int

i = 0
avg = 0
j = 0

interest = int(input("Enter the year of interest: "))
print()

with open("life-expectancy.csv") as life:
    for line in life:
        i = i + 1
        cleanline = line.strip()
        parts = cleanline.split(",")
        if i > 1:
            country = parts[0]
            code = parts[1]
            year = int(parts[2])
            life_expectancy = float(parts[3])
            
            if life_expectancy < lowest:
                lowest = life_expectancy
                place = country
                oldage = year
            if life_expectancy > highest:
                highest = life_expectancy
                highplace = country
                age = year
            
            if interest == year:
                avg = avg + life_expectancy
                j = j + 1
                average = avg / j
                if life_expectancy < minlife:
                    minlife = life_expectancy
                    area = country
                    olddate = year
                if life_expectancy > maxlife:
                    maxlife = life_expectancy
                    higharea = country
                    date = year

print(f"The lowest overall life expectancy is: {lowest}, from {place} in {oldage}")
print(f"The highest life overall expectancy is: {highest}, from {highplace} in {age}")
print()
print(f"For the year {interest}:")
print(f"The average life expectancy was {average:.2f}")
print(f"The maximum life expectancy was {maxlife} in {higharea}")
print(f"The minimum life expectancy was {minlife} in {area}")
print()