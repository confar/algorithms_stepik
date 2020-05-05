import io
import itertools

f = io.StringIO('461531907')


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
    print(len(out))
    print(' '.join(str(i) for i in out))


main(f)
