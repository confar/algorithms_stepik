import sys


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main():
    n = int(sys.stdin.readline())
    print(fib(n))


if __name__ == "__main__":
    main()
