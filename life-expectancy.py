lowest = 999
highest = 0
number = float
i = 0
with open("life-expectancy.csv") as life:
    for line in life:
        i = i + 1
        cleanline = line.strip()
        parts = cleanline.split(",")
        if i > 1:
            for number in parts[3]:
                highest = max(parts[3])
                print(highest)