# pylint: disable=missing-function-docstring, missing-module-docstring
def is_safe(report):
    report = list(map(int, report))

    if report != sorted(report) and report != sorted(report, reverse=True):
        return 0
    # asc
    if report == sorted(report):
        for i in range(len(report) - 1):
            if report[i + 1] - report[i] > 3 or report[i + 1] - report[i] < 1:
                return 0
    # desc
    else:
        for i in range(len(report) - 1):
            if report[i] - report[i + 1] > 3 or report[i] - report[i + 1] < 1:
                return 0
    return 1


def is_safe_with_problem_dampener(report):
    report = list(map(int, report))
    for i in range(len(report)):
        temp = report[:i] + report[i + 1 :]
        if is_safe(temp):
            return 1
    return 0


def main():
    with open("2.txt", "r", encoding="utf-8") as f:
        safe_reports = 0
        safe_reports_with_problem_dampener = 0
        while True:
            lines = f.readline()
            if not lines:
                break
            line = lines.split()
            safe_reports += is_safe(line)
            safe_reports_with_problem_dampener += is_safe_with_problem_dampener(line)

        print("Number of safe reports: ", safe_reports)
        print(
            "Number of safe reports with problem dampener: ",
            safe_reports_with_problem_dampener,
        )


if __name__ == "__main__":
    main()
