import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--count', action='store_true', default=False)
parser.add_argument('--num', action='store_true', default=False)
parser.add_argument('--sort', action='store_true', default=False)
parser.add_argument('source')
try:
    args = parser.parse_args()
    with open(args.source) as f:
        data = list(map(str.strip, f.readlines()))
    if args.sort:
        data.sort()
    if args.num:
        data = list(map(lambda x: f'{x[0]} {x[1]}', enumerate(data)))
    if args.count:
        data.append(f'rows count: {len(data)}')
    print('\n'.join(data))
except Exception as e:
    print('ERROR')
