import math


def latticePaths(grid):
    return math.factorial(2*grid)/(math.factorial(grid) * math.factorial(grid))


print latticePaths(20)
        
