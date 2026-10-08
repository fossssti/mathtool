import argparse

def set_parser():
    parser = argparse.ArgumentParser(prog="mathtool", description = "mathtool - решение уравнений", allow_abbrev= False)
    commands = parser.add_subparsers(dest="command", allow_abbrev= False)

    #solve
    parser_solve = commands.add_parser("solve", help="Решение уравнений ax^2+bx+c=0 ", allow_abbrev= False)   
    parser_solve.add_argument("-a", type=int)
    parser_solve.add_argument("-b", type=int)
    parser_solve.add_argument("-c", type=int)

    #stats
    parser_stats=commands.add_parser("stats", help="Показатели последовательности", allow_abbrev= False)
    parser_stats.add_argument("--input",help="Имя файла с числами")

    #series
    parser_series=commands.add_parser("series", help="сумма ряда", allow_abbrev=False)
    parser_series.add_argument("--func", required=True, help="Имя ряда")
    group = parser_series.add_mutually_exclusive_group(required=True)
    group.add_argument("--terms", type=int, help="Количество слагаемых")
    group.add_argument("--eps", type=float, help="Точность")

    #integrate
    parser_integrate = commands.add_parser("integrate", help="Интегрирование", allow_abbrev=False)
    parser_integrate.add_argument("--func", required=True, help="Имя функции")
    parser_integrate.add_argument("--from", dest="start", type=float, required=True, help="Нижний предел")
    parser_integrate.add_argument("--to", dest="end", type=float, required=True, help="Верхний предел")
    parser_integrate.add_argument("--steps", type=int, required=True, help="Число шагов")

    return parser