"""
File: word_guess.py
-------------------
Fill in this comment.
"""


import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word):
    word_len = len(secret_word)
    remaining_guess = 8
    guessed_word = ""
    for i in range(word_len):
        guessed_word += "_ "
    while "_" in guessed_word and remaining_guess > 0:
        print("The word now looks like this: " + guessed_word)
        print("You have " + str(remaining_guess) + " guesses left")
        character_guess = input("Type a single letter here, then press enter: ")
        if character_guess.casefold() in secret_word.casefold():
            print("That guess is correct.")
            for i in range(len(secret_word)):
                if secret_word[i].casefold() == character_guess.casefold():
                    guessed_word = guessed_word[:2*i] + secret_word[i] + guessed_word[2*i+1:]
        else:
            print("There are no "+character_guess.upper()+"'s in the word")
            remaining_guess -= 1

    if '_' in guessed_word and remaining_guess <= 0:
        print("Sorry, you lost. The secret word was: "+secret_word)
    else:
        print("Congratulations, the word is: "+secret_word)


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    word_list = []
    with open(LEXICON_FILE) as file:
        for line in file:
            word_list.append(line.strip())

    random_word = random.choice(word_list)
    print(random_word)
    return random_word


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()