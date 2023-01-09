if __name__ == "__main__":

    total = 0
    with open("data.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            oppo, me = line.split(" ")
            oppo = oppo.strip()
            me = me.strip()
            if oppo == "A":  # Rock
                if me == "X":
                    total += 3
                elif me == "Y":
                    total += 6
            elif oppo == "B":  # Paper
                if me == "Y":
                    total += 3
                elif me == "Z":
                    total += 6
            elif oppo == "C":  # Scissor
                if me == "X":
                    total += 6
                elif me == "Z":
                    total += 3

            if me == "X":
                total += 1
            elif me == "Y":
                total += 2
            elif me == "Z":
                total += 3

    print(f"Total: {total}")
