result = 0
word_search = []
search = "MAS"
patterns = [
    [(0, 1), (0, 2), (0, 3)],  # Right
    [(0, -1), (0, -2), (0, -3)],  # Left
    [(1, 0), (2, 0), (3, 0)],  # Down
    [(-1, 0), (-2, 0), (-3, 0)],  # Up
    [(1, 1), (2, 2), (3, 3)],  # Down Right
    [(1, -1), (2, -2), (3, -3)],  # Down Left
    [(-1, 1), (-2, 2), (-3, 3)],  # Up Right
    [(-1, -1), (-2, -2), (-3, -3)],  # Up Right
]


def check_patterns(w_pos, c_pos):
    res = 0

    for p in patterns:
        check = False

        for letter in range(len(search)):
            check = validate_check(w_pos + p[letter][0], c_pos + p[letter][1], search[letter])

            if not check:
                break

        if check:
            res += 1

    return res


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
        if word_search[w][c] == "X":
            result += check_patterns(w, c)

print(result)
