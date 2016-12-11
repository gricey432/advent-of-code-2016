import hashlib


# Helper
def md5(s):
    return hashlib.md5(s).hexdigest()


door_id = "ojvtpuvg"  # Magic string from puzzle

result = ''
n = 0
while True:
    r = md5(door_id + str(n))
    if r.startswith('00000'):
        result += r[5]
        if len(result) is 8:
            break
    n += 1

print result
