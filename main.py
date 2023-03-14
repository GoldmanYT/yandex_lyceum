import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--per-day', type=float, default=0)
parser.add_argument('--per-week', type=float, default=0)
parser.add_argument('--per-month', type=float, default=0)
parser.add_argument('--per-year', type=float, default=0)
parser.add_argument('--get-by', choices=['day', 'month', 'year'], type=str, default='day')
args = parser.parse_args()

if args.get_by == 'day':
    print(int(args.per_day + args.per_week / 7 + args.per_month / 30 + args.per_year / 360))
elif args.get_by == 'month':
    print(int(args.per_day * 30 + args.per_week * 30 / 7 + args.per_month + args.per_year / 12))
elif args.get_by == 'year':
    print(int(args.per_day * 360 + args.per_week * 360 / 7 + args.per_month * 12 + args.per_year))
