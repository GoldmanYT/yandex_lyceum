import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--sort', action='store_true', default=False)
parser.add_argument('strs', nargs='*')
args = parser.parse_args()

d = {}
for s in args.strs:
    key, value = s.split('=')
    d[key] = value

if args.sort:
    d = dict(sorted(d.items()))

for key, value in d.items():
    print(f'Key: {key}	Value: {value}')
