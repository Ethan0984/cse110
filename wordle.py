import random
#words = ('casino')
word = "casino"
print('Welcome to Wordle!')
print()
guesses = int
guesses = 0
finish = False
while finish == False:
    guess = input("What is your guess? ").lower()
    if guess != word:
        guesses = guesses + 1
        print("Your guess was not correct")
        if len(guess) != len(word):
            print("Please make your guess the same length as the word")
    else:
        guesses = guesses + 1
        finish = True
    if finish == True:
        break
print(f"You got it in {guesses} guesses!")