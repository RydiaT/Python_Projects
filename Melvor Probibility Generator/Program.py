from random import randint
from Summary import summary


def setup():
    options = []

    options.append(int(input("How many are you going to make normally? ")))
    options.append(int(input("What is the chance of Resource Preservation? ")))
    options.append(int(input("What is the chance of Item Doubling? ")))
    options.append(int(input("How many times to do want to run this? ")))
    options.append((options[1] * options[2]) / 100)

    run(options)


def run(options):
    print("\nRunning...")
    extras = []
    loop = 1

    while loop < options[3]:
        item = 1
        extra = 0

        num_preserved = 0
        num_doubled = 0
        num_both = 0
        actual_runs = 0

        while item < options[0]:

            preserved = False
            doubled = False

            actual_runs += 1

            if randint(1, 100) <= options[1]:
                extra += 1
                item -= 1
                preserved = True

            if randint(1, 100) <= options[2]:
                extra += 1
                doubled = True

            if preserved and doubled:
                num_both += 1
            else:
                if preserved:
                    num_preserved += 1
                if doubled:
                    num_doubled += 1

            item += 1

        extras.append([extra, num_preserved, num_doubled, num_both, actual_runs])
        loop += 1

    print("The tests are done.\n")
    summary(extras, options)
