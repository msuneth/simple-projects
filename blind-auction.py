from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the secret auction program.")
is_other_bidders = True
auction = {}
while is_other_bidders:
    name = input("What is your name?:")
    bid = int(input("What is your bid?: $"))
    auction[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
    if other_bidders == "yes":
        clear()
    elif other_bidders == "no":
        highest_bidder = ""
        highest_bid = 0
        for name in auction:
            bid_amount = auction[name]
            # print(type(int(auction["name"])))
            # print(type(int(highest_bid)))
            if bid_amount > highest_bid:
                highest_bidder = name
                highest_bid = bid_amount
        print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
        is_other_bidders = False
    else:
        print("invalid input")
