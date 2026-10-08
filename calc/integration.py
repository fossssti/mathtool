import math 
MAX_STEPS = 100000

def f_ration(x):
    return x / (x+1)

def f_root(x):
    return math.sqrt(x*x+1)

Integrals = {
    "ratio": (f_ration, "F(x) = x / (x+1)", 0, 20, True),
    "root": (f_root, "F(x) = sqrt(x^2 + 1)", -5, 5, False ),
}

def integrate(func, a, b, steps):
    #Метод левых треугольников
    dx = (b-a)/ steps
    result = 0
    for i in range(steps):
        x = a + i * dx
        result += func(x) * dx
    return result

def handle_integrate(args):
    if not (math.isfinite(args.start) and math.isfinite(args.end)):
        raise ValueError("Ошибка: пределы должны быть конечными числами")
    if args.start >= args.end:
        raise ValueError("Ошибка: начальный предел не меньше конечного")
    if not 1 <= args.steps <= MAX_STEPS:
        raise ValueError("количество шагов вне диапазона")

    fn, formula, low, high, closed = Integrals[args.func]
    if closed:
        ok = low <= args.start and args.end <= high
    else:
        ok = low < args.start and args.end < high
    if not ok:
        raise ValueError("Ошибка: предел вне промежутка")

    print(formula)
    value = integrate(fn, args.start, args.end, args.steps)
    print(f"Значение интеграла: {value:.4f}")
    return 0