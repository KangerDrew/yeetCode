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
