from string import strip

# Compass
N = 'n'
S = 's'
E = 'e'
W = 'w'
compass = [N, E, S, W]

# Load input
with open('1.in', 'r') as f:
    input_str = f.readline().strip()
steps = input_str.split(',')
steps = map(strip, steps)

# Process
x = 0
y = 0
d = 0  # North
for step in steps:
    # Turn
    turn = step[0]
    if turn == 'R':
        d = (d + 1) % 4
    else:
        d = (d - 1) % 4

    # Move
    length = int(step[1:])
    if compass[d] == N:
        y += length
    elif compass[d] == S:
        y -= length
    elif compass[d] == E:
        x += length
    elif compass[d] == W:
        x -= length
    else:
        raise ValueError

# Result
print abs(x) + abs(y)
