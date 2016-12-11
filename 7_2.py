# Read file
with open('7.in', 'r') as f:
    lines = f.readlines()
lines = map(str.strip, lines)


# Helpers
def is_aba(s):
    return s[0] == s[2] and s[0] != s[1]


def aba_to_bab(aba):
    return aba[1] + aba[0] + aba[1]


def supports_ssl(ip):
    # Find ABAs
    abas = []
    out_brackets = [s.split(']')[-1] for s in ip.split('[')]
    for s in out_brackets:
        for n in range(len(s) - 2):
            if is_aba(s[n:n+3]):
                abas.append(s[n:n+3])

    # Find corresponding BAB
    babs = map(aba_to_bab, abas)
    in_brackets = [s.split(']')[0] for s in ip.split('[')[1:]]
    for s in in_brackets:
        for n in range(len(s) - 2):
            if s[n:n+3] in babs:
                return True

    return False


# Process
result = 0
for line in lines:
    if supports_ssl(line):
        result += 1

print result
