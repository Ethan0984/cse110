playagain = bool
playagain = True
phrase = "in coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
while playagain == True:
    number = int(input('Please enter a number: '))
    for i, letter in enumerate(phrase):
        if i % number == 0:
            print(letter.upper(), end="")
        else:
            print(letter.lower(), end="")
    print()
    Play = input("Do you want to play again? ")
    if Play == "yes" or "YES" or "Yes" or "y":
        playagain = True
    elif Play == "no" or "NO" or "n" or "No":
        playagain = False
        break
    else:
        break
print("Thanks for playing!")