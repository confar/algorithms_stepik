import io
from collections import Counter
import operator
import sys

f = io.StringIO('5\n2 3 9 2 9')


def main(str_buffer):
    next(str_buffer)
    c = Counter(next(str_buffer).split())
    out = []
    for char, freq in sorted(c.items(), key=operator.itemgetter(0)):
        out.extend([char for _ in range(freq)])
    print(' '.join(out))
    return out


if __name__ == '__main__':
    assert main(f) == ['2', '2', '3', '9', '9']
