

secret_word = "python"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        if guess_count == 0:
            guess = input("Let's guess the name of a reptile without paws: ")
            guess_count += 1
        elif guess_count == 1:
            guess = input("It's a type of a serpent, huge and sometimes dangerous for human: ")
            guess_count += 1
        elif guess_count == 2:
            guess = input("It's also a name of one of the most popular programing languages: ")
            guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You lose, let's play another time!")
else:
    print("That's right, it's Python!!!")
