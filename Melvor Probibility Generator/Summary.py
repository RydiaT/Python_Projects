from Extras import minimax


def summary(results, options):
    total_extra = 0
    total_preserved = 0
    total_doubled = 0
    total_both = 0
    total_runs = 0
    average_extra = 0
    average_preserved = 0
    average_doubled = 0
    average_both = 0

    for result in results:
        total_extra += result[0]
        total_preserved += result[1]
        total_doubled += result[2]
        total_both += result[3]
        total_runs += result[4]

    average_extra = round(total_extra / options[3])
    average_preserved = round(total_preserved / options[3])
    average_doubled = round(total_doubled / options[3])
    average_both = round(total_both / options[3])

    print(f"The average number of bonus items is %s, for a total of %s items made!" % (average_extra, average_extra + options[0]))
    print("Other Averages:")
    print(f"- Resources Preserved: %s" % average_preserved)
    print(f"- Items Doubled: %s" % average_doubled)
    print(f"- Both: %s" % average_both)

    if input("See bonus statistics? y/n ") == "y":
        minimax(results, [total_preserved, total_doubled, total_both, total_runs])

    if input("See raw data? y/n ") == "y":
        print("Options:")
        print(options)
        for option in options:
            print(f'%s: %s' % (options.index(option), option))
        print("Data:")
        print(results)
