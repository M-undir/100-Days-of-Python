from art import logo
print(logo)

bidding = True

bid_dict = {}

while bidding:
    name = input("What is your name?: ").title()
    bid = float(input("What is your bid?: £"))
    bid_dict[name] = "{:.2f}".format(bid)
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    if other_bidders == 'no':
        bidding = False
        max_value = max(bid_dict, key=bid_dict.get)
        # Built-in method that gets the key with the highest number in a dict
        print(f"The winner is {max_value} with a bid of £{bid_dict[max_value]}")
