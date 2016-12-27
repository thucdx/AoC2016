from helper import *

IS_TEST = False
inp = 'input/day03'

if IS_TEST:
    content = get_content_from_file(inp + '.sample')
else:
    content = get_content_from_file(inp)


def is_triangle(arr):
    arr = list(map(int, arr))
    return 2 * max(arr) < sum(arr)

res = 0
# PART 1
# for pair in content:
#     if is_triangle(pair.split()):
#         res += 1


# PART 2
l = len(content)
for i in range(l):
    content[i] = content[i].split()

for i in range(0, l, 3):
    if i + 2 >= l:
        break
    for j in range(3):
        if is_triangle([content[i][j], content[i + 1][j], content[i + 2][j]]):
            res += 1

print('res: ', res)
