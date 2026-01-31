import art
print(art.logo)

user_data = {}

is_bidding_on = True
while is_bidding_on:
    username = input("Enter your name: ")
    bid_amt = float(input("Enter Bid amount: "))
    user_data[username] = bid_amt

    x = input("Any other bidder?(Y/N)").lower()
    if x == "n":
        is_bidding_on = False
    
def max_bidder_finder(userdata):
    max_bid = 0
    max_user = ""
    for user in user_data:
        if user_data[user] > max_bid:
            max_bid = user_data[user]
            max_user = user
    print(f"\nThe winner bidder is {max_user} whose bid is {max_bid}.")

max_bidder_finder(user_data)