print()
childmeal = float(input("What is the price of a child's meal? "))
adultmeal = float(input("What is the price of an adult's meal? "))
childcount = int(input("How many children are there? "))
adultcount = int(input("How many adults are there? "))
salestax = float(input("What is the sales tax rate? "))
subtotal = childmeal * childcount + adultmeal * adultcount
print()
print("Subtotal:", subtotal)