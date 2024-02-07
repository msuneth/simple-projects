import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

user_input = int(input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0, 2)

if user_input == computer_choice:
    status = "Draw"
elif user_input == 0 and computer_choice == 1:
    status = "You lose"
elif user_input == 0 and computer_choice == 2:
    status = "You won"
elif user_input == 1 and computer_choice == 0:
    status = "You won"
elif user_input == 1 and computer_choice == 2:
    status = "You lose"
elif user_input == 2 and computer_choice == 0:
    status = "You lose"
elif user_input == 2 and computer_choice == 1:
    status = "You won"
else:
    print("Invalid input")
    exit()

choice = [rock,paper,scissors]
print(f"Your choice:{choice[user_input]}")
print(f"Computer choice:{choice[computer_choice]}")
print(status)