import math
import sys

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

def handle_stats(args):
    if args.input:
        with open(args.input, encoding="utf-8") as f:
            tokens = f.read().split()
    else:
        tokens = sys.stdin.read().split()

    if not tokens:
        raise ValueError("Ошибка: последовательность пуста")
    if len(tokens) > 20:
        raise ValueError("Ошибка: чисел больше 20")

    values = []
    for t in tokens:
        try:
            v = float(t)
        except ValueError:
            raise ValueError(f"{t} не является числом")
        if not math.isfinite(v) or abs(v) > 10000:
            raise ValueError("Ошибка: недопустимое значение")
        values.append(v)

    table = [
        ("Количество", len, "d")
        ("Сумма", sum, ".3f")
        ("Ср. арифм.", mean, ".3f")
        ("Сумма кв.", sum_of_squares, ".3f")
        ("Ср. арифм. кв.", root_mean_square, ".3f")
        ("Дисперсия", variance, ".3f")
        ("СКО", standart_deviation, ".3f")
        ("Станд. откл.", sample_standart_deviation, ".3f")
        ("Наименьшее", minimum, ".3f")
        ("Наибольшее", maximum, ".3f")
        ("Положительных", count_positive, "d")
        ("Отрицательных", count_negative, "d")
    ]
    for label, fn, fmt in table:
        v = fn(values)
        if v is None:
            out = "Не существует"
        else:
            out = f"{v:{fmt}}"
        print(f"{label}: {out}")
    return 0

