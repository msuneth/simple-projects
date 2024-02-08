import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = len(stages)
word_list = ["papaya", "mango", "apple"]
chosen_word = random.choice(word_list)

print("chosen word: " + chosen_word)
letter_list = []
for n in range(len(chosen_word)):
    letter_list.append('_')

game_over = False
# correct_chars = 0
while not game_over:
    user_input = input("Guess a letter:").lower()
    incorrect_letter = True
    for n in range(len(chosen_word)):
        char = chosen_word[n]
        if char == user_input:
            letter_list[n] = char
            incorrect_letter = False
            # correct_chars += 1
    guess_letters = ""
    for char in letter_list:
        guess_letters += char
    print(guess_letters)
    if incorrect_letter:
        lives -= 1
        print(stages[lives])
    if '_' not in letter_list:
        # if correct_chars == len(chosen_word):
        print("You win")
        game_over = True
    if lives == 0:
        print("You lose")
        game_over = True
