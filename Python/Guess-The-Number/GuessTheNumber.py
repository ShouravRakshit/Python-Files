import random
def game(number, attempt):
    
    while True:
        print(f"You have {attempt} attempts remaining to guess the number.")
        userInput = int(input("Make a guess: "))
        if userInput < number:
            print("Too low.")
            attempt -= 1
            if attempt == 0:
                print("You've run out of guesses, you lose.")
                break
            print("Guess again")

        elif userInput > number:
            print("Too high.")
            attempt -= 1
            if attempt == 0:
                print("You've run out of guesses, you lose.")
                break
            print("Guess again")

        elif userInput == number:
            print(f"You got it! The answer was {userInput}")
            break

def numberGuess():
    print("Welcome to the Number Guessing Game!")
    print(f"I am thinking of a number a between 1 and 100.")

    random_number = random.randint(1, 100)

    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty_level == "easy":
        game(random_number, 10)

    elif difficulty_level == "hard":
        game(random_number, 5)
    
    else:
        print("Sorry wrong input.")

numberGuess()