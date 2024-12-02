result = 0


def num_within_range(num1, num2):
    diff = int(num1) - int(num2)

    return True if 1 <= abs(diff) <= 3 else False, diff < 0


with open('input.txt') as file:
    while True:
        line = file.readline()

        valid = True
        is_increasing = None

        if not line:
            break

        line = line.strip().split(" ")

        for x in range(0, len(line) - 1):

            diff_valid, increasing = num_within_range(line[x], line[x + 1])

            if not diff_valid:
                valid = False
                break

            if is_increasing is None:
                is_increasing = increasing
            elif is_increasing != increasing:
                valid = False
                break

        if valid:
            result += 1

print(result)
