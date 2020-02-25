def keep_score():
    try:
        p = int(input("How many players are there? "))
    except ValueError:
        p = int(input("Please enter a number: "))
    players = []
    options = ""
    for x in range(p):
        players.append(["", 0])
    for i in range(len(players)):
        players[i][0] = str(input("What is player " + str(i+1) + "'s name? "))
    print(players)
    round = 0

    while 1:
        print("")
        print("r: record scores")
        print("s: see scores")
        print("x: exit program")
        options = input("What would you like to do? ")
        print("")

        if options == "r":
            round += 1
            print("Round " + str(round) + ":")
            for i in range(len(players)):
                try:
                    players[i][1] += int(input("How many points did " + str(players[i][0]) + " earn? "))
                except ValueError:
                    print("Please enter a number.")
                    players[i][1] += int(input("How many points did " + str(players[i][0]) + " earn? "))

        elif options == "s":
            print("")
            for i, x in enumerate(players):
                print(str(players[i][0]) + " has " + str(players[i][1]) + " points")

        elif options == "x":
            print("Game over!")
            print("")
            print("***********************************")
            winning_score = max(y for x, y in players)
            winners = list([x, y] for x, y in players if y == winning_score)
            if len(winners) == 1:
                print(str(winners[0][0]) + " wins with " + str(winners[0][1]) + " points!")
                print("***********************************")
                return players[0]
            elif len(winners) > 1:
                print("It's a tie! "+ " and ".join([x for x, y in winners]) + " tied at " + str(winners[0][1]) + " points!")
                print("***********************************")
                return 0
            return 0

        else:
            print("Please select a valid choice")


keep_score()

exit(0)
