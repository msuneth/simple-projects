import random

logo = """
                                                          /$$     /$$                                                         /$$                          
                                                         | $$    | $$                                                        | $$                          
  /$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$       /$$$$$$  | $$$$$$$   /$$$$$$        /$$$$$$$  /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ 
 /$$__  $$| $$  | $$ /$$__  $$ /$$_____//$$_____/      |_  $$_/  | $$__  $$ /$$__  $$      | $$__  $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$  \ $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$         | $$    | $$  \ $$| $$$$$$$$      | $$  \ $$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$  | $$| $$  | $$| $$_____/ \____  $$\____  $$        | $$ /$$| $$  | $$| $$_____/      | $$  | $$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$      
|  $$$$$$$|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/        |  $$$$/| $$  | $$|  $$$$$$$      | $$  | $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$      
 \____  $$ \______/  \_______/|_______/|_______/          \___/  |__/  |__/ \_______/      |__/  |__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/      
 /$$  \ $$                                                                                                                                                 
|  $$$$$$/                                                                                                                                                 
 \______/   
"""

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def check_answer(answer, guess, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print("You guessed correctly")
        return -1


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

    number_to_be_guessed = random.randint(1, 101)
    print(f"Psst, the number is {number_to_be_guessed}")
    number_of_turns = set_difficulty()
    guess = 0

    while number_to_be_guessed != guess:
        print(f"You have {number_of_turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        number_of_turns = check_answer(number_to_be_guessed, guess, number_of_turns)

        if number_of_turns == -1:
            print(f"The number is {number_to_be_guessed}.\nYou won.")
            return
        elif number_of_turns == 0:
            print(f"You've run out of guesses.\nThe number is {number_to_be_guessed}. you lose.")
            return
        else:
            print("Guess again.")


game()
