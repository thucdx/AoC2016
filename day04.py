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


# return sector_id if room is valid, 0 if not
def get_sector_id(name):
    pattern = '([a-z\-]+)-(\d+)\[(\w+)\]'
    m = re.match(pattern, name)

    if m:
        cksum = checksum(m.group(1))
        if m.group(3) == cksum:
            return int(m.group(2))
    return 0

res = 0
for name in content:
    sector_id = get_sector_id(name)
    print(name, sector_id)
    res += sector_id

print('Result', res)
