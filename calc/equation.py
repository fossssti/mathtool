import math

MAX_VALUE= 10000

def check_coefficients(coefficients):
    #Проверка коэффициентов на допустимый диапазон
    for name, value in coefficients.items():
        if abs(value)> MAX_VALUE:
            raise ValueError("Ошибка: Коэффициент {name} вне допустимого диапозона")

def solve(a, b, c):
       #Решение уравнения 
       if a == 0:
            if b == 0: 
                 raise ValueError("Ошибка: Неизвестное отсутствует, это не уравнение")
            return "Линейное", None, [-c/b]
       else:
            dis = b*b-4*a*c
            if dis > 0:
                 x1=(-b+math.sqrt(dis))/(2*a)
                 x2=(-b-math.sqrt(dis))/(2*a)
                 return "Квадратное", dis, [x1,x2]
            elif dis == 0: 
                 x = -b/(2*a)
                 return "Квадратное", dis, [x]
            else:
                 return "Квадратное", dis, []
           