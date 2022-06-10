from random import randint
import constants as CONSTANTS

def choose_difficulty():
    difficulty = input(CONSTANTS.CHOOSE_DIFFICULTY_PROMPT_MSG).lower()
    while(difficulty != 'easy' and difficulty != 'hard'):
        print(CONSTANTS.CHOOSE_DIFFICULTY_WRONG_ANSWER_MSG)
        difficulty = input(CONSTANTS.CHOOSE_DIFFICULTY_PROMPT_MSG).lower()
    return difficulty

def get_attempts(difficulty):
    if difficulty == 'easy':
        return 10
    return 5

def make_guess():
    guess = None
    while (type(guess) != int):
        try:
            guess = int(input(CONSTANTS.MAKE_GUESS_PROMPT_MSG))
        except:
            print(CONSTANTS.MAKE_GUESS_WRONG_INPUT_TYPE)
    return guess

def is_guess_correct(guess):
    if guess == ANSWER:
        return True
    if guess > ANSWER:
        print(CONSTANTS.TOO_HIGH_MSG)
        return False
    print(CONSTANTS.TOO_LOW_MSG)
    return False

ANSWER = randint(CONSTANTS.MIN_GUESS_RANGE,CONSTANTS.MAX_GUESS_RANGE)
guess_is_correct = False
print(CONSTANTS.ASCII_ART_LOGO)
print(CONSTANTS.WELCOME_MESSAGE)
print(CONSTANTS.CHEAT_ANSWER_MSG(ANSWER))
attempts = get_attempts(choose_difficulty())

while(attempts != 0 and not guess_is_correct):
    print(CONSTANTS.REMAINING_ATTEMPTS_MSG(attempts))
    guess = make_guess() 
    guess_is_correct = is_guess_correct(guess)

    if not guess_is_correct:
        attempts -= 1

if attempts != 0:
    print(CONSTANTS.CORRECT_GUESS_MSG(ANSWER))
else:
    print(CONSTANTS.GAME_OVER_MSG)