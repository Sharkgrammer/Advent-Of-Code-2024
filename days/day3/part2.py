import re

result = 0
pattern = r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)"
allow = True


def parse_match(m):
    # text is mul(0, 0)
    nums = m.strip("mul()").split(",")

    return int(nums[0]) * int(nums[1])


with open('input.txt') as file:
    while True:
        line = file.readline()

        if not line:
            break

        data = re.findall(pattern, line)

        for match in data:
            if "mul" in match:
                if allow:
                    result += parse_match(match)
            else:
                allow = "do()" in match

print(result)
