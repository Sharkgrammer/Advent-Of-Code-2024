import re

result = 0
pattern = r"mul\(\d+,\d+\)"


def parse_match(m):
    # text is mul(0, 0)
    nums = m.strip("mul()").split(",")

    return int(nums[0]) * int(nums[1])


with open('input_test.txt') as file:
    while True:
        line = file.readline()

        if not line:
            break

        data = re.findall(pattern, line)

        for match in data:
            result += parse_match(match)

print(result)
