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
def process(steps):
    # Visited locations
    visited = [(0, 0)]

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
            for i in range(1, length + 1):
                loc = (x, y + i)
                if loc in visited:
                    return abs(x) + abs(y + i)
                visited.append(loc)
            y += length
        elif compass[d] == S:
            for i in range(1, length + 1):
                loc = (x, y - i)
                if loc in visited:
                    return abs(x) + abs(y - i)
                visited.append(loc)
            y -= length
        elif compass[d] == E:
            for i in range(1, length + 1):
                loc = (x + i, y)
                if loc in visited:
                    return abs(x + i) + abs(y)
                visited.append(loc)
            x += length
        elif compass[d] == W:
            for i in range(1, length + 1):
                loc = (x - i, y)
                if loc in visited:
                    return abs(x - i) + abs(y)
                visited.append(loc)
            x -= length
        else:
            raise ValueError

print process(steps)
