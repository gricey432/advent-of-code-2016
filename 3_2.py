from string import split, strip
from operator import add

# Read input
with open('3.in', 'r') as f:
    lines = f.readlines()
lines = map(strip, lines)
lines = map(split, lines)

# Change to 3 numbers coming from columns
transposed = reduce(add, [list(x) for x in zip(*lines)], [])
lines = [transposed[i:i+3] for i in range(0, len(transposed), 3)]

# Test each one
valid = 0
for line in lines:
    a, b, c = map(int, line)
    if a + b > c and a + c > b and b + c > a:
        valid += 1

# Result
print valid
