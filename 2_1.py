from string import strip, split

# Directions
UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'

# Read file
with open('2.in', 'r') as f:
    lines = f.readlines()
lines = map(strip, lines)

# Selections
keypresses = []
x = 1
y = 1
for line in lines:
    for step in line:
        if step == UP:
            y -= 1
        elif step == DOWN:
            y += 1
        elif step == RIGHT:
            x += 1
        elif step == LEFT:
            x -= 1
        else:
            raise ValueError

        # Clamp
        x = max(0, min(2, x))
        y = max(0, min(2, y))

    # Keypush
    keypress = y * 3 + x + 1
    keypresses.append(str(keypress))

# Result
print ''.join(keypresses)
