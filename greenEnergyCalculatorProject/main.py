from argparse import ArgumentParser, Namespace

parser = ArgumentParser()

parser.add_argument("square", help="Squares a given number", type=int)
parser.add_argument("-v", "--verbose", help="Provides a verbose descriptions", type=int, choices=[0, 1, 2])

args: Namespace = parser.parse_args()

if args.verbose:
    print(f"{args.square} squared is: {args.square ** 2}")
else:
    print(args.square ** 2)

