import random
play = bool
play = True
while play == True:
    words = ('casino', 'wordle', 'floats', 'clamor', 'string', 'cheers', 'rivers', 'potato')
    word = random.choice(words).lower()
    print('Welcome to Wordle!')
    print()
    guesses = int
    guesses = 0
    finish = False
    while finish == False:
        guess = input("What is your guess? ").lower()
        for i, letters in enumerate(word):
            if guess[i] == word[i]:
                print(guess[i].upper(), end="")
            elif guess[i] in word:
                print(guess[i], end="")
            else:
                print("_", end="")
        if guess != word:
            guesses = guesses + 1
            print(" is your hint.")
            print()
            if len(guess) != len(word):
                print("Please make your guess the same length as the word")
        else:
            guesses = guesses + 1
            finish = True
        if finish == True:
            break
    print()
    print(f"You got it in {guesses} guesses!")
    playagain = input('Would you like to play again? (y/n) ')
    if playagain == "y":
        play == True
    else: 
        play == False
        print('Thanks for playing!')
        break