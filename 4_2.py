import re

# File
with open('4.in', 'r') as f:
    lines = f.readlines()
lines = map(str.strip, lines)

# Compile regex
pattern = re.compile("(.+)?-(\d+)\[(.+)\]")

# Processing
for line in lines:
    match = pattern.match(line)
    name = match.group(1)
    sector = int(match.group(2))
    hash_ = match.group(3)
    real_name = ''.join(
        ' ' if c == '-'
        else chr((ord(c) - 97 + sector) % 26 + 97)
        for c in name
    )
    if real_name == "northpole object storage":  # Magic string from problem def
        print sector
