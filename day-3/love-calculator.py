WELCOME_MSG = "Welcome to the Love Calculator"
SELF_NAME_PROMPT_MSG = "What's your name?\n"
SIGNIFICANT_OTHER_NAME_PROMPT_MSG = "What's their name?\n"

print(WELCOME_MSG)
self_name = input(SELF_NAME_PROMPT_MSG)
significant_other_name = input(SIGNIFICANT_OTHER_NAME_PROMPT_MSG)

merged_names = (self_name + significant_other_name).lower()

true_score = 0
love_score = 0

true_score += merged_names.count('t')
true_score += merged_names.count('r')
true_score += merged_names.count('u')
true_score += merged_names.count('e')

love_score += merged_names.count('l')
love_score += merged_names.count('o')
love_score += merged_names.count('v')
love_score += merged_names.count('e')

total_score = int(str(true_score) + str(love_score))

if total_score < 10 or total_score > 90:
    final_message = ", you go together like coke and mentos."
elif total_score >= 40 and total_score <= 50:
    final_message = ", you are alright together."
else:
    final_message = '.'
    
print(f"Your score is {total_score}{final_message}")
