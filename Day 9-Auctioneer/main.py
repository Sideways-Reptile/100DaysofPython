from os import system, name
from art import logo

# HINT: You can call clear() to clear the output in the console.
bidPool = {}
still_Bidding = True


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def findHighestBid(bidPool):
    highestBid = 0
    winner = ""
    for auctioner in bidPool:
        bid = bidPool[auctioner]
        if bid > highestBid:
            highestBid = bid
            winner = auctioner
    print(f"The winner is {winner} with a bid of ${highestBid}")


print(logo)
print("Welcome to the Silent Auction.")

while still_Bidding:
    bidder = input("Who is the next bidder? ")
    bid = int(input("What is their bid?: $"))
    bidPool[bidder] = bid
    Restart = input("Are there any more bidders? Type 'yes' or 'no': ")
    if Restart == "no":
        still_Bidding = False
        findHighestBid(bidPool)
    elif Restart == "yes":
        clear()

# print(auctionees)



