list1 = []
list2 = []
result = 0

with open('input.txt') as file:
    while True:
        line = file.readline()

        if not line:
            break

        line = line.strip().split("   ")

        list1.append(int(line[0]))
        list2.append(int(line[1]))

list1.sort()
list2.sort()

for x in range(0, len(list1)):
    result += abs(list1[x] - list2[x])

print(result)
