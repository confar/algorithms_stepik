def gcd(a, b):
    if not a:
        return b
    elif not b:
        return a
    elif a >= b:
        c = a % b
        return gcd(c, b)
    else:
        c = b % a
        return gcd(a, c)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
