def levelOne():

    x = 1
    y = 2

    def levelTwo():

        x = 6
        y = 7

        def levelThree():

            nonlocal x
            nonlocal y
            x = 23
            y = 19

            print("level 3:", x)
            print("level 3:", y)

        levelThree()
        print("level 2:", x)
        print("level 2:", y)

    levelTwo()
    print("level 1:", x)
    print("level 1:", y)


levelOne()
