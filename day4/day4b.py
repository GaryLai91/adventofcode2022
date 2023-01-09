if __name__ == "__main__":
    TOTAL = 0
    with open("data.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            a, b = line.split(",")
            a_min, a_max = a.split("-")
            b_min, b_max = b.split("-")
            a = set([i for i in range(int(a_min), int(a_max) + 1)])
            b = set([i for i in range(int(b_min), int(b_max) + 1)])
            if len(a.intersection(b)) > 0:
                TOTAL += 1
    print(TOTAL)
