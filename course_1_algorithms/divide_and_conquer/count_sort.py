tst1 = [1, 5, 3, 6]
tst2 = [2, 3, 1, 5, 4, 8, 9, 7]


def count_sort(lst):
    count_lst = [0 for _ in range(10)]
    for i in lst:
        count_lst[i] += 1
    for i in range(1, 10):
        count_lst[i] = count_lst[i] + count_lst[i-1]
    out = [None for _ in range(len(lst))]
    for i in lst:
        out[count_lst[i]-1] = i
        count_lst[i] -= 1
    return out


if __name__ == '__main__':
    assert count_sort(tst1) == [1, 3, 5, 6]
    assert count_sort(tst2) == [1, 2, 3, 4, 5, 7, 8, 9]
    assert count_sort([2, 3, 9, 2, 9]) == [2, 2, 3, 9, 9]
