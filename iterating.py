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
    Play = input("Do you want to play again? ").lower()
    if Play == "yes":
        playagain = True
    elif Play == "no":
        playagain = False
        break
    else:
        break
print("Thanks for playing!")