import math

def count(values):
    return len(values)

def sum(values):
    total = 0
    for v in values:
        total += v
    return total

def mean(values):
    if not values:
        return None
    return sum(values) / len(values)

def sum_of_squares(values):
    total = 0
    for v in values:
        total += v*v
    return total

def root_mean_square(values):
    if not values:
        return None
    return math.sqrt(sum_of_squares(values)/len(values))

def variance(values):
    if not values:
        return None
    avg = mean(values)
    total = 0
    for v in values:
        total += (v - avg)**2