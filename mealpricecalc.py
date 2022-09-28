print()
childmeal = float(input("What is the price of a child's meal? "))
adultmeal = float(input("What is the price of an adult's meal? "))
childcount = int(input("How many children are there? "))
adultcount = int(input("How many adults are there? "))
taxrate = float(input("What is the sales tax rate? "))
subtotal = childmeal * childcount + adultmeal * adultcount
print()
print("Subtotal: $" + subtotal)
salestax = taxrate * 0.01 * subtotal
print("Sales Tax: $" + salestax)
total = subtotal + salestax
print("Total: $" + total)
print()
payment = float(input("What is the Payment Amount? "))
change = payment - total
print("Change: $" + change)