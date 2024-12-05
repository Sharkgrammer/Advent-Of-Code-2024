import math

result = 0

rules = {}
manuals = []


def add_rule(rule):
    data = rule.split("|")

    if data[0] in rules:
        rules[data[0]].append(data[1])
    else:
        rules[data[0]] = [data[1]]


def manual_valid(manual):
    # There is no way the first page has a page before it that would violate a rule
    page_list = [manual[0]]

    for page in range(1, len(manual)):
        p = manual[page]

        if p in rules:
            for rule in rules.get(p):
                if rule in page_list:
                    return False

        page_list.append(p)

    return True


def get_middle(manual):
    mid = math.trunc(len(manual) / 2)
    return int(manual[mid])


with open('input.txt') as file:
    rules_compete = False
    while True:
        line = file.readline()

        if not line:
            break

        line = line.strip()

        if rules_compete:
            m_line = line.split(",")
            if manual_valid(m_line):
                result += get_middle(m_line)

        else:
            if line == "":
                rules_compete = True
                continue

            add_rule(line)

print(result)
