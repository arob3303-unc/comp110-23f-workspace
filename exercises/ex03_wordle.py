"""EX03 Wordle Game!"""

__author__ = "730717463"

# Constants - emojis
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


# contains_char function
def contains_char(word: str, character: str) -> bool:
    """Returns True if the letter given is found in the word (False if not)."""
    assert len(character) == 1

    i: int = 0  # counter

    # returns True if character is in word, False if not
    while i < len(word):
        if word[i] == character:
            return True
        i += 1
    return False


# emojified function
def emojified(guess: str, secret: str) -> str:
    """Assigns the emojis in the right spot to let the guesser know if their guessed word is close."""
    assert len(guess) == len(secret)  # User's guess has to equal secret word
    
    empty_str: str = ""  # String that will hold the emoji boxes
    i: int = 0  # counter

    while i < len(secret):

        # elif statements to concatenate to string
        if guess[i] == secret[i]:
            empty_str += GREEN_BOX
        elif contains_char(secret, guess[i]) is True:
            empty_str += YELLOW_BOX
        else:
            empty_str += WHITE_BOX

        i += 1  # adds to counter (ends while loop)

    return empty_str


# input_guess function
def input_guess(num: int) -> str:
    """User enter's their guessed word and it has to be the correct length, if not they try again"""

    word: str = input(f"Enter a {num} character word: ")  # user enter's their word (guess)

    while num != len(word):
        word = input(f"That wasn't {num} chars! Try again: ")  # user tries again if not correct length

    return word


# main function - runs the wordle game!
def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Variables
    secret_word: str = "codes"  # Game's secret word
    turn_num_max: int = 6  # Max turns
    turn_num: int = 1  # Current # of turns

    # Game Loop
    while turn_num <= turn_num_max:

        print(f"=== Turn {turn_num}/{turn_num_max} ===")  # Let's user know how many turns left

        guess_word: str = input_guess(len(secret_word))  # User's guessed word

        print(emojified(guess_word, secret_word))  # Prints emoji boxes

        # elif to let user know if they won/lost
        if secret_word == guess_word:
            print(f"You won in {turn_num}/{turn_num_max} turns!")
            turn_num += turn_num_max

        elif turn_num == turn_num_max:
            print("X/6 - Sorry, try again tomorrow!")
        
        turn_num += 1


if __name__ == "__main__":
    main()