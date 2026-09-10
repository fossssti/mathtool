import math
import sys
#Справка
print("mathtool — решение уравнений вида A*x^2 + B*x + C = 0\nИспользование:\npython mathtool.py -> вывод справки\npython mathtool.py--help -> вывод справки\npython mathtool.py solve -> ввод коэффициентов с клавиатуры\npython mathtool.py solve -a 1 -b 2 -c 2 -> решение с заданными коэффициентами\nКоэффициенты A, B, C - целые числа, по модулю не превышающие 10000"   )
#Получение данных
a = int(input("Введите A: "))
b = int(input("Введите B: "))
c = int(input("Введите C: "))

#Проверка a
try:
    a = int(a)
except ValueError:
    print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
    sys.exit(1)

#Проверка b
try:
    b = int(b)
except ValueError:
    print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
    sys.exit(1)

#Проверка c
try:
    c = int(c)
except ValueError:
    print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
    sys.exit(1)

#Проверка ограничений
if abs(a)>10000 or abs(b)>10000 or abs(c)>10000:
    print('ОШИБКА:значение вне допустимого диапозона')
#Решение
if a == 0:
    if b != 0:
        print("Уравнение не квадратное")
        x = -c/b 
        print("{:.3f}".format(x)) 
    else:
        print("ОШИБКА: это не уравнение, неизвестное отсутствует", file=sys.stderr)
        sys.exit(1)
else:
    print("Уравнение квадратное")
    D = b*b-4*a*c
    print(D)
    if D>0:
        x1 = (-b + math.sqrt(D))/(2*a)
        x2 = (-b - math.sqrt(D))/(2*a)
        print('x1 = ', x1)
        print('x2 = ', x2)
    elif D==0:
        x = -b/(2*a)
        print(x)
    else:
        print("Дейтвительных корней нет")
    