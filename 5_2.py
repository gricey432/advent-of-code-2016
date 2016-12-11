import hashlib


# Helper
def md5(s):
    return hashlib.md5(s).hexdigest()


door_id = "ojvtpuvg"  # Magic string from puzzle

result = [None for _ in range(8)]  # type: list[str]
n = 0
while True:
    r = md5(door_id + str(n))
    if r.startswith('00000'):
        pos = r[5]
        if pos.isdigit() and int(pos) < 8:
            if result[int(pos)] is None:
                result[int(pos)] = r[6]
        if None not in result:
            break
    n += 1

print ''.join(result)
