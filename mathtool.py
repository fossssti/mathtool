import math
import sys
import cli
from calc.equation import handle_solve
from calc.stats import handle_stats
from calc.series import handle_series
from calc.integration import handle_integrate


def main(argv):
    parser = cli.set_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handlers = {
        "solve": handle_solve,
        "stats": handle_stats,
        "series": handle_series,
        "integrate": handle_integrate,
    }
    try:
        return handlers[args.command](args)
    except (ValueError, OSError) as error:
        print(f"Ошибка: {error}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

