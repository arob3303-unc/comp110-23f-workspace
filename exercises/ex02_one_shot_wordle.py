"""EX02 One Shot Wordle - A Guessing Game!"""

__author__ = "730717463"

# the secret word that the user has to guess!
secret_word: str = "python"

# Constants - emojis
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# input for the user's guessed word
user_word: str = input(f"What is your {len(secret_word)}-letter guess? ")

# While Loop to confirm if user's word is 6-letters
while len(user_word) != len(secret_word):
    user_word = input(f"That was not {len(secret_word)} letters! Try again: ")

# while loop variables
i: int = 0
emoji_guess: str = ""

# while loop to assign boxes
while i < len(secret_word):

    # variables for yellow box loop
    wrong_i: bool = False
    alternate_i: int = 0

    # while loop to check for yellow boxes
    while wrong_i != True and alternate_i < len(secret_word):
        if secret_word[alternate_i] == user_word[i]:
            wrong_i = True
        else:
            alternate_i += 1

    # elif statements to concatenate to str
    if user_word[i] == secret_word[i]:
        emoji_guess += GREEN_BOX
    elif wrong_i == True:
        emoji_guess += YELLOW_BOX
    else:
        emoji_guess += WHITE_BOX

    i += 1

# prints the answer
print(emoji_guess)


# if-else statement confirming if word was guessed
if user_word == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
