import os
clear = lambda: os.system('clear')

WELCOME_MSG = "Welcome to the \"Secret Auction\" program"
ASKING_BIDDERS_LEFT_PROMPT_MSG = "Are there any bidders left? (y/n)\n"
BIDDER_NAME_PROMPT_MSG = "Please, enter your name\n"
BID_AMOUNT_PROMPT_MSG = "Enter the amount you want to bid\n"
INVALID_RESPONSE_MSG = "Please, make sure of properly inputting the option"
AUCTION = {
    "bidders": {},
    "lead" : None
}
still_bidding = True

print(WELCOME_MSG)

def bid(name, amount):
    AUCTION["bidders"][name] = amount
    
    if not AUCTION["lead"] or AUCTION["bidders"][name] > AUCTION["bidders"][AUCTION["lead"]]:
        AUCTION["lead"] = name
    
def check_if_should_continue():
    clear()
    answer = input(ASKING_BIDDERS_LEFT_PROMPT_MSG).lower()
    while (answer != 'y') and (answer != 'n'):
        print(INVALID_RESPONSE_MSG, "answer:"+answer)
        answer = input(ASKING_BIDDERS_LEFT_PROMPT_MSG).lower()
    return answer == 'y'

while still_bidding:
    bid(input(BIDDER_NAME_PROMPT_MSG), float(input(BID_AMOUNT_PROMPT_MSG)))
    still_bidding = check_if_should_continue()
    
test = AUCTION["lead"]
last = AUCTION["bidders"][AUCTION["lead"]]
print(f"The winner bid comes from: {test} with a total of: {last}$")