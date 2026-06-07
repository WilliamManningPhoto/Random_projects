
def number_guess():
    import random
    guesses = 3
    number_to_guess = random.randint(1, 10)

    while guesses > 0:
        guess = input("Guess a number between 1 and 10: ")
        if guess == str(number_to_guess):
            print("Congratulations! You guessed the correct number.")
        elif guess < str(number_to_guess):
            print("Too low!")
        elif guess > str(number_to_guess):
            print("Too high!")
        else:
            print("Invalid input.")
        guesses -= 1
        print(f"You have {guesses} guesses left.")
    
    if guesses == 0:
        print(f"Sorry, you've run out of guesses. The correct number was {number_to_guess}.")
    pass

while True:
    number_guess()