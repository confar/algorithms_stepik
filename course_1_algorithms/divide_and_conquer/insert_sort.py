tst1 = [1, 5, 3, 6]
tst2 = [2, 3, 1, 5, 4, 8, 10, 7]


def swap(index1, index2, lst):
    lst[index1], lst[index2] = lst[index2], lst[index1]


def insert_sort(lst):
    for index in range(1, len(lst)):
        cur_index = index
        while cur_index > 0 and lst[cur_index - 1] > lst[cur_index]:
            swap(cur_index-1, cur_index, lst)
            cur_index -= 1
    return lst


if __name__ == '__main__':
    assert insert_sort(tst1) == [1, 3, 5, 6]
    assert insert_sort(tst2) == [1, 2, 3, 4, 5, 7, 8, 10]
