
secret: int = 3
guess: int = 4

if guess == secret:
    print("Success!")
    print(str(guess) + " is the secret number!")
else:
    guess = guess + 1
    if guess == secret:
        print("Success on 2nd try!")
    else:
        print("Wrong Guess. :(")