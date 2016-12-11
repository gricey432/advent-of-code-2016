import re

WIDTH = 50
HEIGHT = 6


screen = [
    [
        0
        for y in range(HEIGHT)
    ]
    for x in range(WIDTH)
]


def rect(w, h):
    for x in range(w):
        for y in range(h):
            screen[x][y] = 1


def rotate_col(col, by):
    for _ in range(by):
        screen[col].insert(0, screen[col][-1])
        del screen[col][-1]


def rotate_row(row, by):
    for _ in range(by):
        tmp = screen[-1][row]
        for x in range(WIDTH - 1, 0, -1):
            screen[x][row] = screen[x-1][row]
        screen[0][row] = tmp


def ps():
    # Print screen
    for x in [list(x) for x in zip(*screen)]:
        print ''.join(
            '#' if c else '.'
            for c in x
        )
    print ''


# Read input
with open('8.in', 'r') as f:
    lines = f.readlines()
lines = map(str.strip, lines)

# Compile regex
p_rect = re.compile("rect (\d+)x(\d+)")
p_rotate_col = re.compile("rotate column x=(\d+) by (\d+)")
p_rotate_row = re.compile("rotate row y=(\d+) by (\d+)")

# Process commands
for line in lines:
    ps()
    print line

    res = p_rect.match(line)
    if res:
        w = int(res.group(1))
        h = int(res.group(2))
        rect(w, h)
        continue

    res = p_rotate_col.match(line)
    if res:
        col = int(res.group(1))
        by = int(res.group(2))
        rotate_col(col, by)
        continue

    res = p_rotate_row.match(line)
    if res:
        row = int(res.group(1))
        by = int(res.group(2))
        rotate_row(row, by)
        continue

ps()
print sum(
    sum(
        1
        for j in i
        if j
    )
    for i in screen
)
