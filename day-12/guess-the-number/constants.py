ASCII_ART_LOGO = """
  / _ \_   _  ___  ___ ___  /__  \|__   ___     /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|  / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/ \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

MIN_GUESS_RANGE = 1
MAX_GUESS_RANGE = 100
WELCOME_MESSAGE = "Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100."
CHOOSE_DIFFICULTY_PROMPT_MSG = "Choose a difficulty. Type 'easy' or 'hard':\n"
CHOOSE_DIFFICULTY_WRONG_ANSWER_MSG = "Please, make sure of typing either 'easy' or 'hard'"
CHEAT_ANSWER_MSG = lambda answer: f"Pssst, the correct answer is {answer}"
MAKE_GUESS_PROMPT_MSG = "Make a guess\n"
MAKE_GUESS_WRONG_INPUT_TYPE = "Please, make sure of introducing a valid integer"
TOO_LOW_MSG = "Too low, guess again"
TOO_HIGH_MSG = "Too high, guess again"
REMAINING_ATTEMPTS_MSG = lambda attempts: f"You have {attempts} attempts remaining to guess the number."
CORRECT_GUESS_MSG = lambda guess: f"You got it! The answer was {guess}."
GAME_OVER_MSG = "You've run out of guesses, you lose."

