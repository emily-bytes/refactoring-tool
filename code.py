def main():
    n, t = 10, 10

    for i in range(1, n + 1):
        if i == 1:
            print(f"{n}, ", end="")

    for i in range(1, t + 1):
        if t == 1:
            print(f"{t}, ", end="")

    return 0

if __name__ == "__main__":
    main()