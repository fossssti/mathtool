import math

MAX_VALUE= 10000


def check_coefficients(coefficients):
    #Проверка коэффициентов на допустимый диапазон
    for name, value in coefficients.items():
        if value is None:
            raise ValueError(f"коэффициент {name} не задан")
        if abs(value)> MAX_VALUE:
            raise ValueError(f"Ошибка: Коэффициент {name} вне допустимого диапозона")

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

def handle_solve(args):
    if args.a is None and args.b is None and args.c is None:
        try:
            args.a= int(input("Введите A: "))
            args.b= int(input("Введите B: "))
            args.c= int(input("Введите C: "))
        except ValueError:
            raise ValueError("Ошибка: коэффициент не является целым числом")
    elif None in (args.a, args.b, args.c):
        raise ValueError("Ошибка: укажите все три коэффциента либо ни одного")

    check_coefficients({"A": args.a, "B": args.b, "C": args.c})
    kind, dis, roots = solve(args.a, args.b, args.c)

    print(f"Уравнение {kind}")
    if dis is not None:
        print(f"Дискриминант {dis}")
    if not roots:
        print("Действительных корней нет")
    else:
        for i, x in enumerate(roots, 1):
            if len(roots) > 1:
                name = f"x{i}"
            else:
                name = "x"
            print(f"{name} = {x:.3f}")
    return 0

               