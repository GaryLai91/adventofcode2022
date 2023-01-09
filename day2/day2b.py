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
                    # I need to lose
                    total += 3
                elif me == "Y":
                    # I need to draw
                    total += 3
                    total += 1
                elif me == "Z":
                    # I need to win
                    total += 6
                    total += 2
            elif oppo == "B":  # Paper
                if me == "X":
                    total += 1
                elif me == "Y":
                    total += 2
                    total += 3
                elif me == "Z":
                    total += 3
                    total += 6
            elif oppo == "C":  # Scissor
                if me == "X":
                    total += 2
                elif me == "Y":
                    total += 3
                    total += 3
                elif me == "Z":
                    total += 6
                    total += 1

    print(f"Total: {total}")
