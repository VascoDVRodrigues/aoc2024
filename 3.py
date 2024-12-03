# pylint: disable=missing-function-docstring, missing-module-docstring
import re

def get_mul_result(lines, expression):
    mul_sum = 0
    multiply = True

    lines = [line.replace("\n", "") for line in lines]
    for line in lines:
        matches = re.findall(expression, line)
        for match in matches:
            if match == "do()":
                multiply = True
            elif match == "don't()":
                multiply = False
            else:
                a, b = map(int, match[4:-1].split(","))
                if 0<a<1000 and 0<b<1000 and multiply:
                    mul_sum += a * b
    return mul_sum

def main():
    with open("3.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        pattern = r"mul\(\d+,\d+\)"
        mul_result = get_mul_result(lines, pattern)

        pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
        conditional_mul_result = get_mul_result(lines, pattern)

    print("Result of multiplication: ", mul_result)
    print("Result of conditional multiplication: ", conditional_mul_result)

if __name__ == "__main__":
    main()
