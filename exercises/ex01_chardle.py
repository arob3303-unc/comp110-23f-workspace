"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730717463"

# User inputs

five_character_word: str = input("Enter a 5-character word: ")
# Exit program and display error message
if len(five_character_word) != 5:
    print("Error: Word must contain 5 characters.")
    exit()

single_character: str = input("Enter a single character: ")
# Exit program and display error message
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()

# Diagnostic message confirming variables
print("Searching for " + single_character + " in " + five_character_word)

# Counts how many characters are in the word
index_counter: int = 0

# if statements for single character
if five_character_word[0] == single_character:
    print(single_character + " found at index 0")
    index_counter += 1

if five_character_word[1] == single_character:
    print(single_character + " found at index 1")
    index_counter += 1

if five_character_word[2] == single_character:
    print(single_character + " found at index 2")
    index_counter += 1

if five_character_word[3] == single_character:
    print(single_character + " found at index 3")
    index_counter += 1

if five_character_word[4] == single_character:
    print(single_character + " found at index 4")
    index_counter += 1

# if statements for counter
if index_counter == 0:
    print("No instances of " + single_character + " found in " + five_character_word)

if index_counter == 1:
    print(str(index_counter) + " instance of " + single_character + " found in " + five_character_word)

if index_counter > 1:
    print(str(index_counter) + " instances of " + single_character + " found in " + five_character_word)