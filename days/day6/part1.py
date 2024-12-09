class Pos:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


result = 0

g_map = []
guard = None
max_pos = None
direction = 0


def inside_map():
    return (0 <= guard.x <= max_pos.x) and (0 <= guard.y <= max_pos.y)


def move_valid():
    try:
        match direction:
            case 0:
                if g_map[guard.y - 1][guard.x] != "#":
                    return True
            case 1:
                if g_map[guard.y][guard.x + 1] != "#":
                    return True
            case 2:
                if g_map[guard.y + 1][guard.x] != "#":
                    return True
            case 3:
                if g_map[guard.y][guard.x - 1] != "#":
                    return True
    except IndexError:
        # should only happen as they leave
        return True


with open('input.txt') as file:
    y = 0
    max_x = 0

    while True:
        line = file.readline()

        if not line:
            break

        line = list(line.strip())
        g_map.append(line)

        if guard is None:
            check = 0

            try:
                check = line.index('^')
            except ValueError:
                check = -1

            if check != -1:
                guard = Pos(check, y)
                max_x = len(line) - 1

        y += 1

    max_pos = Pos(max_x, y - 1)

while inside_map():
    if g_map[guard.y][guard.x] != "X":
        g_map[guard.y][guard.x] = "X"
        result += 1

    if not move_valid():
        if direction == 3:
            direction = 0
        else:
            direction += 1
    else:
        match direction:
            case 0:
                guard.y -= 1
            case 1:
                guard.x += 1
            case 2:
                guard.y += 1
            case 3:
                guard.x -= 1

print(result)
