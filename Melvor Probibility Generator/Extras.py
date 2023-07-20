def minimax(data, totals):

    minimum = 999
    for run in data:
        if run[0] < minimum:
            minimum = run[0]

    maximum = -999
    for run in data:
        if run[0] > maximum:
            maximum = run[0]

    difference = maximum - minimum

    actual_preserved = ((totals[0] + totals[2]) / totals[3]) * 100
    actual_doubled = ((totals[1] + totals[2]) / totals[3]) * 100
    actual_both = (totals[2] / totals[3]) * 100

    print("\nBonus Stats:")
    print(f"- Minimum Extra: %s" % minimum)
    print(f"- Maximum Extra: %s" % maximum)
    print(f"- Range Extra: %s" % difference)
    print(f"- Resources Preserved Chance: %s" % round(actual_preserved, 2))
    print(f"- Items Doubled Chance: %s" % round(actual_doubled, 2))
    print(f"- Both Chance: %s\n" % round(actual_both, 2))
