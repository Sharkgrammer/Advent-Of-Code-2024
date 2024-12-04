result = 0
word_search = []

# This isn't my prettiest work. Sorry
patterns = [
    [  # Top Left to Bottom Right
        [
            [(-1, -1), "M"],
            [(1, 1), "S"]
        ],
        [
            [(-1, -1), "S"],
            [(1, 1), "M"]
        ],
    ],
    [  # Top Right to Bottom Left
        [
            [(-1, 1), "M"],
            [(1, -1), "S"]
        ],
        [
            [(-1, 1), "S"],
            [(1, -1), "M"]
        ],
    ]
]


def check_patterns(w_pos, c_pos):
    point_check = 0

    for p in patterns:
        point_valid = False

        for points in p:
            if point_valid:
                break

            start = points[0]
            end = points[1]

            if validate_check(w_pos + start[0][0], c_pos + start[0][1], start[1]):
                if validate_check(w_pos + end[0][0], c_pos + end[0][1], end[1]):
                    point_check += 1
                    point_valid = True

        if not point_valid:
            break

    return point_check == 2


def validate_check(w_pos, c_pos, letter):
    if w_pos < 0 or w_pos >= len(word_search):
        return False

    if c_pos < 0 or c_pos >= len(word_search[w_pos]):
        return False

    return word_search[w_pos][c_pos] == letter


with open('input.txt') as file:
    while True:
        line = file.readline()

        if not line:
            break

        word_search.append(line.strip())

for w in range(len(word_search)):
    for c in range(len(word_search[w])):
        if word_search[w][c] == "A":
            if check_patterns(w, c):
                result += 1

print(result)
