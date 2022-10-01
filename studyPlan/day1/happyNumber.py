# While the definition of happy number is pretty straight forward, break condition can
# seem bit confusing. The break condition is, whenever we find a new sum by adding the
# squares of the digits, we add it to a hash set to mark that we've already covered
# that particular sum value. Infinite loop will occur when during the summing of squared
# digits, we run into a number that we've already processed!

