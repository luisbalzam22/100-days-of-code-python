from random import choice
import hangman_art
import hangman_words
import os
clear = lambda: os.system('clear')
clear()

LETTER_PROMPT_MSG = "Please, enter a letter\n"
INITIAL_LIVES_COUNT = 6

end_of_game = False
total_lives = INITIAL_LIVES_COUNT
random_word = choice(hangman_words.word_list)
letters_left_to_guess = len(random_word)
guessed_letters = ['_'] * len(random_word) # !: how to initialize an n-length array

print(hangman_art.logo)

while (not end_of_game):
    print(guessed_letters)
    current_letter = input(LETTER_PROMPT_MSG).lower()
    clear()
    new_letter_was_guessed = False

    for index in range(0, len(random_word)):
        if current_letter == random_word[index] and current_letter != guessed_letters[index]:
            new_letter_was_guessed = True
            guessed_letters[index] = current_letter
    
    if current_letter in guessed_letters:
        if new_letter_was_guessed:
            print(f"You just guessed the letter {current_letter}\n\n")
        else:
            print("You already guessed that letter\n\n")
    else:
        total_lives -=1
        
    print(hangman_art.stages[total_lives])
    if total_lives == 0 or '_' not in guessed_letters:
        end_of_game = True

if(total_lives > 0):
    print('You won! :)')
else:
    print('You lose :(')