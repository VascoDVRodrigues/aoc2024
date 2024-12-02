# pylint: disable=missing-function-docstring, missing-module-docstring


def main():
    with open("1.txt", "r", encoding="utf-8") as f:
        cumulative_difference = 0
        list1 = []
        list2 = []
        while True:
            lines = f.readline()
            if not lines:
                break

            d1, d2 = lines.split()
            list1.append(int(d1))
            list2.append(int(d2))
        list1 = sorted(list1)
        list2 = sorted(list2)

        for i, _ in enumerate(list1):
            cumulative_difference += abs(list1[i] - list2[i])

        print("Distance between lists: ", cumulative_difference)
        similarity = 0
        for value in list1:
            count = list2.count(value)
            similarity += count * value

        print("Similarity between lists: ", similarity)


if __name__ == "__main__":
    main()
