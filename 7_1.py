# Read file
with open('7.in', 'r') as f:
    lines = f.readlines()
lines = map(str.strip, lines)


# Helpers
def is_abba(s):
    return s[0] == s[3] and s[1] == s[2] and s[0] != s[1]


def supports_tls(ip):
    # False if abba in brackets
    in_brackets = [s.split(']')[0] for s in ip.split('[')[1:]]
    for s in in_brackets:
        for n in range(len(s) - 3):
            if is_abba(s[n:n+4]):
                return False

    # True if abba out of brackets
    out_brackets = [s.split(']')[-1] for s in ip.split('[')]
    for s in out_brackets:
        for n in range(len(s) - 3):
            if is_abba(s[n:n+4]):
                return True

    # False default
    return False


# Process
result = 0
for line in lines:
    if supports_tls(line):
        result += 1

print result
