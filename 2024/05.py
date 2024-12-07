def is_valid(rules: list, page: list) -> bool:
    for rule in rules:
        if rule[0] in page and rule[1] in page:
            idx_0 = page.index(rule[0])
            idx_1 = page.index(rule[1])
            if idx_0 > idx_1:
                return False
    return True


def order_page(rules: list, page: list) -> list:
    n_rules = len(rules)
    while n_rules > 0:
        for rule in rules:
            if rule[0] in page and rule[1] in page:
                idx_0 = page.index(rule[0])
                idx_1 = page.index(rule[1])
                if idx_0 > idx_1:
                    page.pop(idx_0)
                    page.insert(idx_1, rule[0])
                else:
                    n_rules -= 1
            else:
                continue
    return page


### Part 1
# Example
with open("2024/data/05_example.txt", "r") as f:
    manual = f.readlines()
    manual = [l.strip() for l in manual]
    manual_rules = [tuple(int(r) for r in m.split("|")) for m in manual if "|" in m]
    manual_pages = [
        list(int(r) for r in m.split(",")) for m in manual if m and "|" not in m
    ]

middle_pages = 0
for page in manual_pages:
    if is_valid(manual_rules, page):
        middle_pages += page[int((len(page) - 1) / 2)]
print("Example 1:", middle_pages)

# Puzzle
with open("2024/data/05_input.txt", "r") as f:
    manual = f.readlines()
    manual = [l.strip() for l in manual]
    manual_rules = [tuple(int(r) for r in m.split("|")) for m in manual if "|" in m]
    manual_pages = [
        list(int(r) for r in m.split(",")) for m in manual if m and "|" not in m
    ]

middle_pages = 0
for page in manual_pages:
    if is_valid(manual_rules, page):
        middle_pages += page[int((len(page) - 1) / 2)]
print("Puzzle 1:", middle_pages)

### Part 2 - convolution approach
# Example
with open("2024/data/05_example.txt", "r") as f:
    manual = f.readlines()
    manual = [l.strip() for l in manual]
    manual_rules = [tuple(int(r) for r in m.split("|")) for m in manual if "|" in m]
    manual_pages = [
        list(int(r) for r in m.split(",")) for m in manual if m and "|" not in m
    ]

middle_pages = 0
for page in manual_pages:
    if not is_valid(manual_rules, page):
        ordered_page = order_page(manual_rules, page)
        middle_pages += ordered_page[int((len(ordered_page) - 1) / 2)]
print("Example 2:", middle_pages)


# Puzzle
with open("2024/data/05_input.txt", "r") as f:
    manual = f.readlines()
    manual = [l.strip() for l in manual]
    manual_rules = [tuple(int(r) for r in m.split("|")) for m in manual if "|" in m]
    manual_pages = [
        list(int(r) for r in m.split(",")) for m in manual if m and "|" not in m
    ]

middle_pages = 0
for page in manual_pages:
    if not is_valid(manual_rules, page):
        ordered_page = order_page(manual_rules, page)
        middle_pages += ordered_page[int((len(ordered_page) - 1) / 2)]
print("Puzzle 2:", middle_pages)
