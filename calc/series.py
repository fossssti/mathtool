import math

MAX_TERMS = 10000
MAX_EPS = 0.0001
MAX_ITERATIONS = 100000

def sign(n):
    return 1 if n%2 == 1 else -1

def term_sqplus(n):
    return sign(n)/(n*n+1)

def term_third(n):
    return sign(n)/ (3*n)

FORMULAS = {
    "sqplus": (term_sqplus, "S = 1/(1^2+1) - 1/(2^2+1) + 1/(3^2+1) - ..."),
    "third": (term_third, "S = 1/3 - 1/6 + 1/9 - 1/12 + ..."),
}

def sum_by_terms(term_func, count):
    #Сумма ряда по кол-ву слагаемых (слагаемое, количество)
    result = 0
    for n in range(1, count+1):
        result += term_func(n)
    return result

def sum_by_eps(term_func, eps):
    #Сумма по точности(слагаемое, eps)
    result = 0
    n = 0
    while True:
        n += 1 
        value = term_func(n)
        result += value
        if abs(value) < eps:
            return result, n
        if n >=MAX_ITERATIONS:
            raise ValueError("Ошибка: точность не достигнута")

def handle_series(args):
    if args.eps is not None:
        if not (math.isfinite(args.eps) and 0 < args.eps <= MAX_EPS):
            raise ValueError("Ошибка: точность вне диапазона")
    if args.terms is not None:
        if not 1 <= args.terms <= MAX_TERMS:
            raise ValueError("Ошибка: количество слагаемых вне диапазона")

    term, formula = FORMULAS[args.func]
    print(formula)

    if args.terms is not None:
        result = sum_by_terms(term, args.terms)
        n = args.terms
    else:
        result, n = sum_by_eps(term, args.eps)

    print(f"Слагаемых: {n}")
    print(f"Сумма ряда: {result:.4f}")
    return 0