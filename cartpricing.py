items = []
selection = None
print("Welcome to the Shopping Cart Program!")
print()
while selection != "5":
    print()
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    selection = input("Please enter an action: ")

    if selection == "1":
        newitem = input("What item would you like to add? ")
        items.append(newitem)
        print(f"'{newitem}' has been added to the cart.")
    if selection == "2":
        print("The contents of the cart are: ")
        for item in items:
            print(item)
print("Thank you. Goodbye.")