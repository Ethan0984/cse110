items = []
thing = None
print("Please enter the items of the shopping list:")
while thing != 'quit':
    thing = input("Item: ")
    if thing != 'quit':
        items.append(thing)
print()
print("The shopping list is:")
for item in items:
    print(item)
print()
print("The list with indexes is:")
for i in range(len(items)):
    item = items[i]
    print(f"{i}. {item}")