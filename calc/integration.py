import math 
MAX_STEPS = 100000

def f_ration(x):
    return x / (x+1)

def f_root(x):
    return math.sqrt(x*x+1)

Integrals = {
    "ration": (f_ration, "F(x) = x / (x+1)", 0, 20, True),
    "root": (f_root, "F(x) = sqrt(x^2 + 1)", -5, 5, False ),
}

def integrate(func, a, b, steps):
    dx = (b-a)/ steps
    result = 0
    for i in range(steps):
        x = a + i * dx
        result += func(x) * dx
    return result