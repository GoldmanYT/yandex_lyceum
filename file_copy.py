import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--upper', action='store_true', default=False)
parser.add_argument('--lines', type=int)
parser.add_argument('source')
parser.add_argument('destination')
args = parser.parse_args()

with open(args.source) as f:
    data = f.readlines()
    if args.lines is not None:
        n = max(0, min(args.lines, len(data)))
    else:
        n = len(data)
    if args.upper:
        res = list(map(str.upper, data[:n]))
    else:
        res = data[:n]

with open(args.destination, 'w') as f:
    f.writelines(res)
