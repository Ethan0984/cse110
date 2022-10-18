print()
loan = False
print('Answer 1-10 for the Following:')
large = int(input('How large is the loan? '))
credit = int(input('How good is your credit history? '))
income = int(input('How high is your income? '))
payment = int(input('How large is your down payment? '))
if large >= 5:
    if credit >= 7  and income >= 7:
        loan = True
    elif credit >= 7 or income >= 7:
        if payment >= 5:
            loan = True
        else:
            loan = False
    else:
        loan = False
else:
    if credit < 4:
        loan = False
    if income >= 7 or payment >= 7:
        loan = True
    elif income >= 4 and payment >= 4:
        loan = True
    else:
        loan = False