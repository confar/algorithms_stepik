import itertools

import io
# tst1 = io.StringIO('10 2')
tst1 = io.StringIO('1598753 25897')


def fib_mod(n, m):
    mod_arr = [0, 1]
    a, b = mod_arr
    period_found = False
    for _ in range(2, (6 * m) + 1):
        a, b = b, a + b
        mod_arr.append(b % m)
        if mod_arr[-2:] == [0, 1]:
            period_found = True
            break
    period = (len(mod_arr) - 2)
    if period_found:
        return mod_arr[n % period]
    return mod_arr[period]


def main(str_buffer):
    n, m = map(int, next(str_buffer).split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main(tst1)