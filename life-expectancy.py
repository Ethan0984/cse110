lowest = 999
highest = -1
place = ""
highplace = ""
age = int
oldage = int
i = 0
with open("life-expectancy.csv") as life:
    for line in life:
        i = i + 1
        cleanline = line.strip()
        parts = cleanline.split(",")
        if i > 1:
            #time = int(input("Enter the year of interest: "))
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
print(f"The lowest overall life expectancy is: {lowest}, from {place} in {oldage}")
print(f"The highest life overall expectancy is: {highest}, from {highplace} in {age}")