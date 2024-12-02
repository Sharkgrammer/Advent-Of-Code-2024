result = 0


def num_within_range(num1, num2):
    diff = int(num1) - int(num2)

    return True if 1 <= abs(diff) <= 3 else False, diff > 0


def validate_data(data):
    is_increasing = None
    for x in range(0, len(data) - 1):
        diff_valid, increasing = num_within_range(data[x], data[x + 1])

        if not diff_valid:
            return False

        if is_increasing is None:
            is_increasing = increasing

        elif is_increasing != increasing:
            return False

    return True


with open('input.txt') as file:
    while True:
        line = file.readline()

        if not line:
            break

        line = line.strip().split(" ")

        validated = validate_data(line)

        if not validated:
            for i in range(0, len(line)):
                tempLine = list(line)
                del tempLine[i]

                if validate_data(tempLine):
                    validated = True
                    break

        if validated:
            result += 1

print(result)
