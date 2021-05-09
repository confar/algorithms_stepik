"""
Различные слагаемые

По данному числу 1 <= n <= 10^9 найдите максимальное число k,
для которого n можно представить как сумму k различных натуральных слагаемых.
Выведите в первой строке число k, во второй — k слагаемых.
"""

import io
import itertools

test1 = io.StringIO('461531907')


def main(str_buffer):
    num = float(next(str_buffer).strip())
    out = []
    for i in itertools.count(start=1):
        if not num:
            break
        if num - i >= 0:
            out.append(i)
            num -= i
        elif num - i < 0:
            num += out[-1]
            out[-1] = i
            num -= i
    length = len(out)
    print(length)
    print(' '.join(str(i) for i in out))
    return length


if __name__ == "__main__":
    assert main(test1) == 30381
