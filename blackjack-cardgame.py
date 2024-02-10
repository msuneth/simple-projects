import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealer_hand = []
    user_hand = []

    def compare_hand():
        user_sum = 0
        computer_sum = 0
        for card in user_hand:
            user_sum += card
        for card in dealer_hand:
            computer_sum += card
        print(f"Your final hand: {user_hand}, final score: {user_sum}")
        print(f"Computer's final hand: {dealer_hand}, final score: {computer_sum}")
        if user_sum > 21:
            print("You went over. You lose")
        elif user_sum > computer_sum:
            print("You won")
        else:
            print("You lose")
        return "n"

    def show_info():
        user_sum = 0
        for card in user_hand:
            user_sum += card
        if user_sum < 21:
            print(f"Your cards: {user_hand}, current score: {user_sum}")
            print(f"Computer's first card: {dealer_hand[0]}")
        else:
            compare_hand()

    def draw_card(number_of_cards):
        for n in range(number_of_cards):
            dealer_hand.append(cards[random.randint(0, len(cards))])
            user_hand.append(cards[random.randint(0, len(cards))])
        show_info()

    print(logo)
    new_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
    if new_game == "y":
        draw_card(2)
        another_card = "y"
        while another_card == "y":
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if another_card == "y":
                draw_card(1)
        compare_hand()
        blackjack()
    else:
        print("Good bye")


blackjack()
