import math
current_const = []
num_const = 0


def distance(x, y):
    sum = 0
    for i in range(0, 4):
        sum += math.fabs(x[i] - y[i])
    return sum


def process_line(ln):
    global num_const
    nm = ln.split(",")
    nmi = [int(n) for n in nm]
    NEW = True
    for point in current_const:
        if distance(point, nmi) <= 3:
            NEW = False
            break
    if NEW:
        num_const += 1
    current_const.append(nmi)


f = open("constellations.txt", "r+")
for line in f:
    process_line(line)
print(num_const)
