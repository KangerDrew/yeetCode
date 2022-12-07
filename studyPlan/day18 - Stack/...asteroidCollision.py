# Use stack data structure to store incoming asteroids.

# HINT: Collision will only occur, if during the for loop, we encounter (incoming asteroid)
# a negative asteroid and our previous asteroid value was positive!!
# Furthermore, if the incoming asteroid is positive and recent asteroid was negative, they
# will not collide since they would have already be moving away from one another!


def asteroidCollision(asteroids):

    res = []

    for a in asteroids:

        while res and res[-1] > 0 and a < 0:

            # First scenario - Incoming asteroid a is bigger than
            # the one coming in from the left:
            if res[-1] < abs(a):
                # left asteroid is destroyed. While loop will continue and
                # we will need to check if "a" will continue rampaging through
                # remaining asteroids in res stack:
                res.pop()
            # Second scenario - Incoming asteroid is smaller than the one
            # coming in from left. It gets obliterated!
            elif res[-1] > abs(a):
                a = 0
            # Last scenario - The two asteroids are the same size. "a" gets destroyed
            # along with the asteroid that flew in (res[-1])
            else:
                a = 0
                res.pop()

