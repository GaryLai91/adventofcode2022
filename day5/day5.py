if __name__ == "__main__":
    with open("data.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
