import string

if __name__ == "__main__":
    lower_points = dict(
        zip(string.ascii_lowercase, range(1, len(string.ascii_lowercase) + 1))
    )

    upper_points = dict(
        zip(
            string.ascii_uppercase, range(27, len(string.ascii_uppercase) + 27)
        )
    )
    print(lower_points)
    print(upper_points)
    TOTAL = 0
    with open("data.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            first_half = line[: len(line) // 2]
            second_half = line[len(line) // 2 :]
            intersect = set(first_half).intersection(second_half)
            key = intersect.pop()
            try:
                TOTAL += lower_points[key]
            except KeyError:
                TOTAL += upper_points[key]

    print(TOTAL)
