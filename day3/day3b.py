import string
from itertools import islice

if __name__ == "__main__":
    lower_points = dict(
        zip(string.ascii_lowercase, range(1, len(string.ascii_lowercase) + 1))
    )

    upper_points = dict(
        zip(
            string.ascii_uppercase, range(27, len(string.ascii_uppercase) + 27)
        )
    )

    TOTAL = 0
    with open("data.txt", "r") as f:
        while True:
            lines_gen = islice(f, 3)
            chunk = list(lines_gen)
            chunk = [i.strip() for i in chunk]
            if not chunk:
                break
            key = (set(chunk[0]) & set(chunk[1]) & set(chunk[2])).pop()
            try:
                TOTAL += lower_points[key]
            except KeyError:
                TOTAL += upper_points[key]

    print(TOTAL)
