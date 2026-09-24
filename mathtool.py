import math
import sys
import cli

d=10000
#Справка
print(sys.argv)
try:
    if len(sys.argv)== 0  or sys.argv[1] == "--help":
        print("mathtool — решение уравнений вида A*x^2 + B*x + C = 0\nИспользование:\npython mathtool.py -> вывод справки\npython mathtool.py--help -> вывод справки\npython mathtool.py solve -> ввод коэффициентов с клавиатуры\npython mathtool.py solve -a 1 -b 2 -c 2 -> решение с заданными коэффициентами\nКоэффициенты A, B, C - целые числа, по модулю не превышающие 10000"   )
        sys.exit(0)
except IndexError:
    print("ОШИБКА")
    sys.exit(1)

if sys.argv[1] != "solve":
    print("ОШИБКА: Неизвестный код")
    sys.exit(1)
elif len(sys.argv) == 2 and sys.argv[1] == "solve":
   a = int(input("Введите A: "))
   b = int(input("Введите B: "))
   c = int(input("Введите C: "))
elif len(sys.argv)== 8:
    if sys.argv[2]!= "-a" and sys.argv[4]!= "-b" and sys.argv[6]!= "-c":
        print("Неизвестный параметр")
        sys.exit(1)
    a=sys.argv[3]
    b=sys.argv[5]
    c=sys.argv[7]
else:
    print("Неверный набор параметров")
    sys.exit(1)
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
if abs(a)>d or abs(b)>d or abs(c)>d:
    print('ОШИБКА:значение вне допустимого диапозона')
    sys.exit(1)
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
        print('x1 = ', "{:.3f}".format(x1))
        print('x2 = ', "{:.3f}".format(x2))
    elif D==0:
        x = -b/(2*a)
        print("x = ", "{:.3f}".format(x))
    else:
        print("Дейтвительных корней нет")
