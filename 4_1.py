import re
from collections import Counter

# File
with open('4.in', 'r') as f:
    lines = f.readlines()
lines = map(str.strip, lines)

# Compile regex
pattern = re.compile("(.+)?-(\d+)\[(.+)\]")


# Hash generator
def gen_hash(s):
    s = s.replace('-', '')
    items = Counter(s).items()
    items.sort(key=lambda r: r[0])
    items.sort(key=lambda r: r[1], reverse=True)
    return ''.join(i[0] for i in items[:5])

# Processing
total = 0
for line in lines:
    match = pattern.match(line)
    name = match.group(1)
    sector = int(match.group(2))
    hash_ = match.group(3)
    if gen_hash(name) == hash_:
        total += sector

print total
