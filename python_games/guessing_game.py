from random import randint as r

# Game where you guess a number between 1 and 100 within 10 tries.


def guessing_game():
    print("Welcome.")

    answer = r(1, 100)
    win = False
    tries = 0
    response = ""

    while not win and tries != 10:

        check = int(input("Guess a number between 1 and 100."))

        if check == answer:
            win = True
        elif check > answer:
            print("That is too high.")
            tries += 1
        elif check < answer:
            print("That is too low.")
            tries += 1

    if win:
        response = "Congratulations, You won in %i tries." % tries
    elif tries == 10:
        response = "L + Ratio. The answer was %i." % answer

    print(response)
