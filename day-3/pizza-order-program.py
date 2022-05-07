WELCOME_MSG = "Welcome to the Pizza Order Program"
PIZZA_SIZE_PROMPT_MSG = "What size do you want your pizza to be? S: Small, M: Medium, L: Large\n"
ADD_PEPPERONI_PROMPT_MSG = "Do you want to add Pepperoni to your pizza? Y: Yes, N: no\n"
ADD_EXTRA_CHEESE_PROMPT_MSG = "Do you want to add Extra Cheese to your pizza? Y: Yes, N: no\n"

print(WELCOME_MSG)
pizza_size = input(PIZZA_SIZE_PROMPT_MSG).upper()
add_pepperoni = input(ADD_PEPPERONI_PROMPT_MSG).upper()
add_extra_cheese = input(ADD_EXTRA_CHEESE_PROMPT_MSG).upper()

if pizza_size == 'S':
    total_bill = 15
elif pizza_size == 'M':
    total_bill = 20
else:
    total_bill = 25
    
if add_pepperoni == 'Y':
    if pizza_size == 'S':
        total_bill +=2
    else:
        total_bill +=3

if add_extra_cheese == 'Y':
    total_bill +=1

print(f"Total bill: ${total_bill}")