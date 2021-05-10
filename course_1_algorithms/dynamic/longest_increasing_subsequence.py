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
    subsequence_lengths = [1] * len_lst
    for i, value in enumerate(lst):
        for j in range(i):
            if lst[j] < value and subsequence_lengths[j] + 1 > subsequence_lengths[i]:
                subsequence_lengths[i] = subsequence_lengths[j] + 1
    ans = max(subsequence_lengths) if len_lst else 0
    return ans, subsequence_lengths


def longest_non_decreasing_subsequence(str_buffer):
    next(str_buffer)
    lst = [int(i) for i in next(str_buffer).split(' ')]
    len_lst = len(lst)
    subsequence_lengths = [1] * len_lst
    for j in range(1, len_lst):
        for i in range(j+1):
            if lst[i] <= lst[j] and subsequence_lengths[j] + 1 > subsequence_lengths[i]:
                subsequence_lengths[i] = subsequence_lengths[j] + 1
    ans = max(subsequence_lengths) if len_lst else 0
    print(ans)
    print(subsequence_lengths)
    return ans, subsequence_lengths


def longest_non_decreasing_subsequence_by_modulo(lst):
    len_lst = len(lst)
    d = [1] * len_lst
    for i, value in enumerate(lst):
        for j in range(i):
            if lst[j] <= value and not value % lst[j] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    ans = max(d)
    return ans


def main():
    arr = [3, 6, 7, 12]
    assert longest_non_decreasing_subsequence_by_modulo(arr) == 3
    assert longest_increasing_subsequence([]) == (0, [])
    assert longest_increasing_subsequence(arr) == (4, [1, 2, 3, 4])
    assert (longest_increasing_subsequence([7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1]) == 
            (5, [1, 1, 1, 2, 3, 3, 4, 1, 2, 4, 4, 5, 3, 5, 1]))
    assert restore_sequence_from_index_list(5, [1, 1, 1, 2, 3, 3, 4, 1, 2, 4, 4, 5, 3, 5, 1],
                                            [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1]) == [1, 3, 4, 5, 8]


if __name__ == '__main__':
    main()