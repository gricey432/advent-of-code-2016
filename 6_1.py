from collections import Counter

# Read file
with open('6.in', 'r') as f:
    lines = f.readlines()
lines = map(str.strip, lines)

# Process
print ''.join([c.most_common(1)[0][0] for c in map(Counter, [list(x) for x in zip(*lines)])])
