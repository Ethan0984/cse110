youngest = 999
young = ""
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
for line in people:
    cleanline = line.strip()
    part = cleanline.split(" ")
    name = part[0]
    age = int(part[1])
    print(cleanline)
    if age < youngest:
        youngest = age
        young = name
print(f"The youngest person is {young}, who is {youngest} years old.")