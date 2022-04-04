from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the secret auction program.")

### WORKS, BUT CAN PROBABLY BE REFACTORED WITH FUNCTIONS
# auction = {}

# name = input("What is your name?: ")
# bid = input("What's your bid?: $")
# auction[name] = bid
# other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
# while other_bidders == "yes":
#   clear()
#   name = input("What is your name?: ")
#   bid = input("What's your bid?: $")
#   auction[name] = bid
#   other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()  
# else:
#   max_bid = max(auction.values())
#   clear()
#   print(f"The winner is {name} with the highest bid of ${max_bid}.")


### REFACTORED SOLUTION, IMO MORE COMPLICATED VARIABLES. I THINK MY ABOVE SOLUTION IS EASIER TO READ.
auction = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}.")

while not bidding_finished:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  auction[name] = bid
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(auction)
  elif should_continue == "yes":
    clear()