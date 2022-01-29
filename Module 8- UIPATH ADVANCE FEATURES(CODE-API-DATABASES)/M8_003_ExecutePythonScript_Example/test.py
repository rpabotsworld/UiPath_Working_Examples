# Return the sum of square of first n natural numbers
def squaresum(n):
    sm = 0
    for i in range(1, n + 1):
        sm = sm + (i * i)
    return sm