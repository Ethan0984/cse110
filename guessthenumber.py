import random
playagain = "yes"
while playagain == "yes" or "y":
    attempts = 0
    number = random.randint(1,100)
    guess = 0
    print(f"The magic number is {number}")
    while number >= 1 and number <= 100:
        guess = int(input("What is your guess? "))
        if guess < number:
            print("Higher")
            attempts = attempts + 1
        elif guess > number:
            print("Lower")
            attempts = attempts + 1
        else:
            print("You guessed it!")
            break
    print(f"You got it in {attempts} tries")
    playagain = input("Would you like to play again? ")
    if playagain == "no":
        print("Thanks for playing!")