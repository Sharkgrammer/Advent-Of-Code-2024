keys = []
sim_dict = {}
score = 0


def add_to_dict(val, obj):
    obj[val] = obj[val] + 1 if val in obj else 1


with open('input') as file:
    while True:
        line = file.readline()

        if not line:
            break

        line = line.strip().split("   ")

        keys.append(line[0])
        add_to_dict(line[1], sim_dict)

for key in keys:
    if key in sim_dict:
        score += int(key) * sim_dict.get(key)

print(score)
