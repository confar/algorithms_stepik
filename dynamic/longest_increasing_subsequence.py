import io
from collections import deque


def restore_sequence_from_index_list(num, idx_list, orig_list):
    increasing = deque([])
    for i, value in enumerate(reversed(idx_list)):
        if value == num:
            increasing.appendleft(-i-1)
            num -= 1
    out = []
    for i in increasing:
        out.append(orig_list[i])
    return out


def longest_increasing_subsequence(lst):
    len_lst = len(lst)
    d = [1] * len_lst
    for i, value in enumerate(lst):
        for j in range(i):
            if lst[j] < value and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    ans = max(d)
    return ans, d


def longest_non_decreasing_subsequence_by_modulo(lst):
    len_lst = len(lst)
    d = [1] * len_lst
    for i, value in enumerate(lst):
        for j in range(i):
            if lst[j] <= value and not value % lst[j] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    ans = max(d)
    return ans


def test():
    assert longest_increasing_subsequence(
        [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1]) == (5, [1, 1, 1, 2, 3, 3, 4, 1, 2, 4, 4, 5, 3, 5, 1])
    assert restore_sequence_from_index_list(5, [1, 1, 1, 2, 3, 3, 4, 1, 2, 4, 4, 5, 3, 5, 1],
                                               [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1]) == [1, 3, 4, 5, 8]


tst1 = io.StringIO('4\n3 6 7 12')


def main():
    test()
    next(tst1)
    arr = list(map(int, next(tst1).split()))
    assert longest_non_decreasing_subsequence_by_modulo(arr) == 3


if __name__ == '__main__':
    main()