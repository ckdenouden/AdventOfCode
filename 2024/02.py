def is_increasing(report: list) -> bool:
    for idx in range(len(report) - 1):
        if report[idx] >= report[idx + 1]:
            return False
    return True


def is_decreasing(report: list) -> bool:
    for idx in range(len(report) - 1):
        if report[idx] <= report[idx + 1]:
            return False
    return True


def is_good_diff(report: list) -> bool:
    for idx in range(len(report) - 1):
        diff = abs(report[idx] - report[idx + 1])
        if diff < 1 or diff > 3:
            return False
    return True


def is_safe(report: list, dampener: bool = False) -> bool:
    report_increases = is_increasing(report)
    report_decreases = is_decreasing(report)
    report_good_diff = is_good_diff(report)
    if (report_increases or report_decreases) and report_good_diff:
        return True

    if dampener:
        for idx in range(len(report)):
            report_perm = report[:idx] + report[idx + 1 :]
            report_perm_increases = is_increasing(report_perm)
            report_perm_decreases = is_decreasing(report_perm)
            report_perm_good_diff = is_good_diff(report_perm)
            if (
                report_perm_increases or report_perm_decreases
            ) and report_perm_good_diff:
                return True
        return False
    return False


# Example 1
with open("2024/data/02_example.txt", "r") as f:
    reports = f.readlines()
    reports = [l.strip() for l in reports]
reports_clean = [[int(r2) for r2 in r1.split(" ")] for r1 in reports]

safe = 0
for report in reports_clean:
    safe += is_safe(report)
print("Example 1:", safe)


# Puzzle 1
with open("2024/data/02_input.txt", "r") as f:
    reports = f.readlines()
    reports = [l.strip() for l in reports]
reports_clean = [[int(r2) for r2 in r1.split(" ")] for r1 in reports]

safe = 0
for report in reports_clean:
    safe += is_safe(report)
print("Puzzle 1:", safe)


# Example 2
with open("2024/data/02_example.txt", "r") as f:
    reports = f.readlines()
    reports = [l.strip() for l in reports]
reports_clean = [[int(r2) for r2 in r1.split(" ")] for r1 in reports]

safe = 0
for report in reports_clean:
    safe += is_safe(report, dampener=True)
print("Example 2:", safe)


# Puzzle 2
with open("2024/data/02_input.txt", "r") as f:
    reports = f.readlines()
    reports = [l.strip() for l in reports]
reports_clean = [[int(r2) for r2 in r1.split(" ")] for r1 in reports]

safe = 0
for report in reports_clean:
    safe += is_safe(report, dampener=True)
print("Puzzle 2:", safe)
