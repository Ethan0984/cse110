accounts = []
balances = []
print("Enter the names and balances of bank accounts (type quit when done):")
bank = None
while bank != 'quit':
    bank = input('What is the name of the account? ')
    if bank != 'quit':
        accounts.append(bank)
    if bank == 'quit':
        break
    money = input('What is the balance? ')
    balances.append(money)
print()
print('Account Information:')
for i in range(len(accounts)):
    account = accounts[i]
    balance = balances[i]
    print(f"{account} - ${balance}")