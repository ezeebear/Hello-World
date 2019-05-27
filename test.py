import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', type=float, default=0.0,
                        help='What is the first number?')
    parser.add_argument('-y', type=float, default=0.0,
                        help='What is the second number?')
    parser.add_argument('-z', type=float, default=0.0,
                        help='What is the third number?')
    parser.add_argument('-op', type=str, default='',
                        help='What operation?(add, sub, mul, div, km_to_miles, miles_to_km, fah_to_cel, cel_to_fah, cm_to_inch, inch_to_cm, sqroot)')
    args = parser.parse_args()
    print(args)
    ans = calc(args)
    print('The solution is: {0}'.format(ans))

def calc(args):
    if args.op == 'add':
        return args.x + args.y + args.z
    elif args.op == 'sub':
        return args.x - args.y - args.z
    elif args.op == 'mul':
        return args.x * args.y
    elif args.op == 'div':
        return args.x / args.y / args.z
    elif args.op == 'km_to_miles':
        return args.x / 1.609
    elif args.op == 'miles_to_km':
        return args.x * 1.609
    elif args.op == 'cm_to_inch':
        return args.x / 2.54
    elif args.op == 'inch_to_cm':
        return args.x * 2.54
    elif args.op == 'cel_to_fah':
        return (args.x * 9/5) + 32
    elif args.op == 'fah_to_cel':
        return (args.x - 32) * 5/9
    elif args.op == 'sqroot':
        return args.x ** 0.5

if __name__ == '__main__':
    main()
