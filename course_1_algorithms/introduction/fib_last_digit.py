def fib_last_digit(n):
    a, b = 0, 1
    for _ in range(n):
        j = (b % 10)
        a, b = j, (a % 10) + j
    return a


def main():
    n = int(input())
    print(fib_last_digit(n))


if __name__ == "__main__":
    main()
