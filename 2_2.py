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
x = 0
y = 2
for line in lines:
    for step in line:
        if step == UP:
            if y > abs(x - 2):
                y -= 1
        elif step == DOWN:
            if y < 4 - abs(x - 2):
                y += 1
        elif step == LEFT:
            if x > abs(y - 2):
                x -= 1
        elif step == RIGHT:
            if x < 4 - abs(y - 2):
                x += 1
        else:
            raise ValueError

    # Keypush
    keypress = 0
    for i in range(y):
        keypress += 1 + 2 * (2 - abs(i - 2))
    keypress += x - abs(y - 2) + 1
    if keypress < 10:
        keypresses.append(str(keypress))
    else:
        keypresses.append(chr(65 + keypress - 10))

# Result
print ''.join(keypresses)
