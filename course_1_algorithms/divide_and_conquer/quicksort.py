import io


def swap(lst, index1, index2):
    lst[index1], lst[index2] = lst[index2], lst[index1]


def partition(lst, start, end):
    pivot = lst[end]
    wall = start
    for i in range(start, end):
        if lst[i] <= pivot:
            swap(lst, i, wall)
            wall += 1
    swap(lst, wall, end)
    return wall


def quick_sort_recursive(lst, start, end):
    if start >= end:
        return lst
    pivot = partition(lst, start, end)
    quick_sort_recursive(lst, start, pivot - 1)
    quick_sort_recursive(lst, pivot + 1, end)
    return lst


tst1 = io.StringIO('8\n7 2 5 3 7 13 1 6')
tst2 = io.StringIO('7\n7 6 5 4 3 2 1')
tst3 = io.StringIO('5\n1 2 3 5 4')
tst4 = io.StringIO('5\n1 3 4 5 6 2')
tst5 = io.StringIO('5\n2 3 9 2 9')


def get_list_from_buffer(str_buffer):
    _ = next(str_buffer)
    lst = [int(i) for i in next(str_buffer).strip().split(' ')]
    return lst


if __name__ == '__main__':
    lst1 = get_list_from_buffer(tst1)
    lst2 = get_list_from_buffer(tst2)
    lst3 = get_list_from_buffer(tst3)
    lst4 = get_list_from_buffer(tst4)
    lst5 = get_list_from_buffer(tst5)
    assert quick_sort_recursive(lst1, 0, len(lst1) - 1) == [1, 2, 3, 5, 6, 7, 7, 13]
    assert quick_sort_recursive(lst2, 0, len(lst2) - 1) == [1, 2, 3, 4, 5, 6, 7]
    assert quick_sort_recursive(lst3, 0, len(lst3) - 1) == [1, 2, 3, 4, 5]
    assert quick_sort_recursive(lst4, 0, len(lst4) - 1) == [1, 2, 3, 4, 5, 6]
    assert quick_sort_recursive(lst5, 0, len(lst5) - 1) == [2, 2, 3, 9, 9]
