f = open('input/day01', 'r')

content = f.read()
if not content:
    print("empty content! Check again!")

instructions = content.split(", ")
print(instructions)

x, y, d = 0, 0, 0
vx = [0, -1, 0, 1]
vy = [1, 0, -1, 0]

s = set()
s.add((x, y))
found = False

for instruction in instructions:
    if found:
        break

    d = (d + [-1, 1][instruction[0] == 'R']) % 4
    step = int(instruction[1:])

    for i in range(step):
        x, y = x + vx[d], y + vy[d]
        if s.__contains__((x, y)):
            found = True
            print('Result', abs(x) + abs(y))
            break
        else:
            s.add((x, y))
