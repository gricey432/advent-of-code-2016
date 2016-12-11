from string import split, strip

# Read input
with open('3.in', 'r') as f:
    lines = f.readlines()
lines = map(strip, lines)
lines = map(split, lines)

# Test each one
valid = 0
for line in lines:
    a, b, c = map(int, line)
    if a + b > c and a + c > b and b + c > a:
        valid += 1

# Result
print valid

