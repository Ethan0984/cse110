print()
childmeal = float(input("What is the price of a child's meal? "))
adultmeal = float(input("What is the price of an adult's meal? "))
childcount = int(input("How many children are there? "))
adultcount = int(input("How many adults are there? "))
taxrate = float(input("What is the sales tax rate? "))
subtotal = childmeal * childcount + adultmeal * adultcount
print()
print(f'Subtotal: ${subtotal:.2f}')
salestax = taxrate * 0.01 * subtotal
print(f'Sales Tax: ${salestax:.2f}')
total = subtotal + salestax
print(f'Total: ${total:.2f}')
print()
payment = float(input("What is the Payment Amount? "))
change = payment - total
print(f'Change: ${change:.2f}')