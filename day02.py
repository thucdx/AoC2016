from helper import *

IS_TEST = False
if IS_TEST:
    content = get_content('input/day02.sample')
else:
    content = get_content('input/day02')


# keypad = ['123', '456', '789']
keypad = ['##1##', '#234#', '56789', '#ABC#', '##D##']
move = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}

start = '5'
row, col = -1, -1

for i in range(len(keypad)):
    for j in range(len(keypad[i])):
        if keypad[i][j] == start:
            row, col = i, j
            break
res = ''
for line in content:
    for c in line:
        new_row, new_col = row + move[c][0], col + move[c][1]
        if 0 <= new_row < len(keypad) and 0 <= new_col < len(keypad[0]) and keypad[new_row][new_col] != '#':
            row, col = new_row, new_col
    res += keypad[row][col]

print('Result: ', res)
