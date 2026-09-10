import math
import sys
#Справка

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
if a==0 and b==0:
    print("Не является уравнением")
if a == 0:
    if b != 0:
        print("Уравнение не квадратное")
        x = -c/b 
        print(round(x,3)) 
    