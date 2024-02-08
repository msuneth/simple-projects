alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text, shift_num):
    encrypt_text = ""
    for char in plain_text:
        char_index = alphabet.index(char)
        encrypt_char_index = char_index + shift_num
        if encrypt_char_index < 26:
            encrypt_text += alphabet[char_index + shift_num]
        else:
            encrypt_text += alphabet[26 - (char_index + shift_num)]
    print("Here's the encoded result: " + encrypt_text)


def decrypt(encrypt_text, shift_num):
    plain_text = ""
    for char in encrypt_text:
        char_index = alphabet.index(char)
        decrypt_char_index = char_index - shift_num
        if decrypt_char_index < 0:
            plain_text += alphabet[(char_index - shift_num)+26]
        else:
            plain_text += alphabet[char_index - shift_num]
    print("The decoded text is: " + plain_text)


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Invalid input")
        exit()