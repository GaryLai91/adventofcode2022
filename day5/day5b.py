if __name__ == "__main__":
    rows, cols = (8, 9)
    table = [[0 for col in range(cols)] for row in range(rows)]
    with open("data.txt") as f:
        # process stacks
        for row in range(rows):
            line = f.readline()
            arr = []
            for i in range(0, 36, 4):
                arr.append(line[i : i + 4].strip())
            table[row] = arr

        t = [[0 for row in range(rows)] for col in range(cols)]
        for i in range(len(table)):
            for j in range(len(table[0])):
                t[j][i] = table[i][j]

        for row in range(len(t)):
            t[row] = t[row][::-1]
            t[row] = [i[1] for i in t[row] if i]

        # read lines that are not useful
        _ = f.readline()
        _ = f.readline()

        # read instructions
        while True:
            line = f.readline()
            if not line:
                break
            line = line.split(" ")
            steps, head, tail = int(line[1]), int(line[3]), int(line[5])
            print(f"Next line: {steps, head, tail}")

            items = ""
            for i in range(steps):
                item = t[head - 1].pop()
                items += item
            items = items[::-1]
            items = [i for i in items]
            t[tail - 1].extend(items)

        result = ""
        for i in range(len(t)):
            try:
                result += t[i][-1]
            except IndexError:
                continue
        print(result)

