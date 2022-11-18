items = []
prices = []
selection = None
print("Welcome to the Shopping Cart Program!")
print()
while selection != "6":
    print()
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Compute average")
    print("6. Exit")
    selection = input("Please enter an action: ")

    if selection == "1":
        newitem = input("What item would you like to add? ")
        items.append(newitem)
        newprice = float(input(f"What is the price of {newitem}? "))
        prices.append(newprice)
        print(f"'{newitem}' has been added to the cart.")
    elif selection == "2":
        print("The contents of the cart are: ")
        for i in range(len(items)):
            item = items[i]
            price = prices[i]
            print(f"{i + 1}. {item} - ${price:.2f}")
    elif selection == "3":
        for i in enumerate(items):
            index = int(input("Which item would you like to remove? ")) - 1
            user_choice = items[index]
            items.remove(user_choice)
            print("Item removed")
    elif selection == "4":
        total = sum(prices)
        print(f"Your total price is ${total:.2f}")
    elif selection == "5":
        average = total/len(prices)
        print(f"The average cost of your items is ${average:.2f}")
    else:
        if selection != "6":
            print("Please enter a number 1-6")
print("Thank you. Goodbye.")