def fibonacci_rabbits(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        # We use dynamic programming to calculate the number of rabbit pairs
        # alive after each month, given the number from the previous two months
        rabbits = [1, 1]
        for i in range(2, n):
            rabbits.append(rabbits[i-1] + (rabbits[i-2] * k))
        return rabbits[-1]
