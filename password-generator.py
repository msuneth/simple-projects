# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_length = nr_letters + nr_symbols + nr_numbers
password = ""

for n in range(0, password_length):
    random_char = random.randint(0, 2)
    if random_char == 0:
        random_letter = letters[random.randint(0, len(letters) - 1)]
        password += str(random_letter)
    elif random_char == 1:
        random_symbol = symbols[random.randint(0, len(symbols) - 1)]
        password += str(random_symbol)
    else:
        # random_number = numbers[random.randint(0, len(numbers) - 1)]
        random_number = random.choice(numbers)
        # random.shuffle(list_of_chars)
        password += str(random_number)

print(f"Here is your password: {password}")
