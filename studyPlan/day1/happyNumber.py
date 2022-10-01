# While the definition of happy number is pretty straight forward, break condition can
# seem bit confusing. The break condition is, whenever we find a new sum by adding the
# squares of the digits, we add it to a hash set to mark that we've already covered
# that particular sum value. Infinite loop will occur when during the summing of squared
# digits, we run into a number that we've already processed!


def happyNum(n):

    covered = set()
    newVal = n

    while newVal not in covered:

        covered.add(newVal)
        temp = 0
        newValArr = [int(i) for i in str(newVal)]

        for val in newValArr:
            temp += val ** 2

        if temp == 1:
            return True

        newVal = temp

    return False


# Same, but slightly modified approach:
def happyNumAlt(n):

    def sumOfSquares(val):
        output = 0

        while val:
            digit = val % 10
            output += digit ** 2
            val = val // 10

        return output

    checked = set()

    while n not in checked:
        checked.add(n)
        n = sumOfSquares(n)

        if n == 1:
            return True

    return False


# Additional Side Note: this problem can be solved using linked list cycle approach!
