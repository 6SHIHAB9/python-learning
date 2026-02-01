from art import logo
print(logo)
bidders = {}

while True:
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    flow = input("Are there any other bidders? Type \"yes\" or \"no\"\n")

    if flow == "no":
        highest_bid = 0
        winner = ""
        for key in bidders:
            if bidders[key] > highest_bid:
                highest_bid = bidders[key]
                winner = key
        print(f"The winner is {winner} with a bid of ${highest_bid} ")
        break

    print("\n" * 100)