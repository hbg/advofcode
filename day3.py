import math


def manhattan_dist(instructions):
    lines = {
        "x": [],
        "y": []
    }
    current_point = [0, 0]
    for instruction in instructions:
        mag = int(instruction[1:])
        pre = instruction[0]
        print(pre, mag)
        if pre == "D":
            lines["x"].append({
                current_point[0]: {
                    "l": current_point[1] - mag,  # lower bound
                    "u": current_point[1]  # upper bound
                }
            })
            current_point[1] -= mag
        elif pre == "U":
            lines["x"].append({
                current_point[0]: {
                    "l": current_point[1],
                    "u": current_point[1] + mag
                }
            })
            current_point[1] += mag
        elif pre == "R":
            lines["y"].append({
                current_point[1]: {
                    "l": current_point[0],
                    "u": current_point[0] + mag
                }
            })
            current_point[0] += mag
        else:
            lines["y"].append({
                current_point[1]: {
                    "l": current_point[0] - mag,
                    "u": current_point[0]
                }
            })
            current_point[0] -= mag
    print(lines)
    return lines


f = open("test.txt", "r+")
arrows = []
for wire in f:
    arrows.append(manhattan_dist(wire.split(",")))
mn = 9999
comparator = arrows[0]
for y_range_dict in comparator["x"]:
    fixed_x = list(y_range_dict.keys())[0]  # Fixed x value
    y_rng = list(y_range_dict.values())[0]  # Range of y values from first arrow
    for arrow in arrows:
        for d in arrow["y"]:
            fixed_y = list(d.keys())[0]  # Fixed y value from comparator
            x_rng = list(d.values())[0]
            if fixed_y > y_rng["l"] and fixed_y < y_rng["u"]:
                if fixed_x < x_rng["u"] and fixed_x > x_rng["l"]:
                    print("Found at ", fixed_x, fixed_y)
                    curr = math.fabs(fixed_x) + math.fabs(fixed_y)
                    if curr < mn:
                        mn = curr
                    print("Found at ", fixed_y, fixed_x)

for x_range_dict in comparator["y"]:
    fixed_y = list(x_range_dict.keys())[0]
    x_rng = list(x_range_dict.values())[0]
    for arrow in arrows:
        for d in arrow["x"]:
            fixed_x = list(d.keys())[0]
            y_rng = list(d.values())[0]
            if fixed_x > x_rng["l"] and fixed_x < x_rng["u"]:
                if fixed_y < y_rng["u"] and fixed_y > y_rng["l"]:
                    print("Found at ", fixed_x, fixed_y)
                    curr = math.fabs(fixed_x) + math.fabs(fixed_y)
                    if curr < mn:
                        mn = curr
print(mn)
