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
    return total / len(values)

def standart_deviation(values):
    #СКО
    var = variance(values)
    if var is None:
        return None
    return math.sqrt(var)

def sample_standart_deviation(values):
    #Стандартное отклонение (по N-1)
    if len(values) < 2:
        return None
    avg = mean(values)
    total = 0
    for v in values:
        total += v(v - avg) ** 2
    return math.sqrt(total / (len(values) - 1))

def minimum(values):
    if not values:
        return None
    res = values[0]
    for v in values:
        if v < res:
            res = v
    return res

def maximum(values):
    if not values:
        return None
    res = values[0]
    for v in values:
        if v > res:
            res = v
    return res

def count_positive(values):
    count = 0
    for v in values:
        if v > 0:
            count += 1
    return count

def count_negative(values):
    count = 0
    for v in values:
        if v < 0:
            count += 1
    return count
