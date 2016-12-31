from helper import *
import re

IS_TEST = False
inp = 'input/day04'

if IS_TEST:
    content = get_content_from_file(inp + '.sample')
else:
    content = get_content_from_file(inp)


def checksum(txt):
    m = {c: txt.count(c) for c in set(txt)}
    m.pop('-')

    return ''.join([c[0] for c in sorted(m.items(), key=lambda x: (-x[1], x[0]))][:5])


def cipher(txt, shift):
    res = ''
    total = ord('z') - ord('a') + 1
    for c in txt:
        if 'a' <= c <= 'z':
            res += chr((ord(c) - ord('a') + shift + total) % total + ord('a'))
        else:
            res += ' '
    return res


# return sector_id if room is valid, 0 if not
def get_sector_id(name):
    pattern = '([a-z\-]+)-(\d+)\[(\w+)\]'
    m = re.match(pattern, name)

    if m:
        cksum = checksum(m.group(1))
        if m.group(3) == cksum:
            return int(m.group(2))
    return 0


def decode(name):
    pattern = '([a-z\-]+)-(\d+)\[(\w+)\]'
    m = re.match(pattern, name)

    if m:
        cksum = checksum(m.group(1))
        if m.group(3) == cksum:
            return cipher(m.group(1), int(m.group(2)))
    return 'Invalid'

res = 0
for name in content:
    decoded = decode(name)
    print(decode(name))
    if decoded.find('northpole') >= 0:
        print('FOUND: ', name)
        break
