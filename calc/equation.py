import math

MAX_VALUE= 10000

def check_coefficients(coefficients):
    for name, value in coefficients.items():
        if abs(value)> MAX_VALUE:
            raise ValueError("Коэффициент {name} вне допустимого диапозона")

def solve(a, b, c):
           