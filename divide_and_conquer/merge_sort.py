import io
from collections import deque
from enum import Enum
from functools import partial


def merge(lst1, lst2, inverse_count=0):
    out = []
    index1, end1 = 0, len(lst1)
    index2, end2 = 0, len(lst2)
    while True:
        if lst1[index1] <= lst2[index2]:
            out.append(lst1[index1])
            index1 += 1
        else:
            out.append(lst2[index2])
            index2 += 1
            inverse_count += end1 - index1
        if index1 == end1:
            out.extend(lst2[index2:])
            break
        elif index2 == end2:
            out.extend(lst1[index1:])
            break
    return out, inverse_count


def merge_sort_recursive(lst, inverse_count=0):
    sorted_lst, inverse_count = _merge_sort_recursive(lst, inverse_count)
    print(inverse_count)
    return sorted_lst, inverse_count


def _merge_sort_recursive(lst, inverse_count=0):
    len_lst = len(lst)
    if len_lst > 1:
        middle = len_lst // 2
        first, inverse_count = _merge_sort_recursive(lst[0: middle], inverse_count)
        second, inverse_count = _merge_sort_recursive(lst[middle:], inverse_count)
        return merge(first, second, inverse_count)
    else:
        return lst, inverse_count


def merge_sort_iterative(lst):
    queue = deque([])
    for i in lst:
        queue.append([i])
    while len(queue) > 1:
        new_elem, _ = merge(queue.popleft(), queue.popleft())
        queue.append(new_elem)
    return queue[0]


class Call(Enum):
    iterative = partial(merge_sort_iterative)
    recursive = partial(merge_sort_recursive)

    def __str__(self):
        return self.name


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
    import argparse

    parser = argparse.ArgumentParser(description='Merge sort')
    parser.add_argument('call', type=lambda call: Call[call], choices=list(Call), default='iterative')
    args = parser.parse_args()
    call = args.call
    lst1 = get_list_from_buffer(tst1)
    lst2 = get_list_from_buffer(tst2)
    lst3 = get_list_from_buffer(tst3)
    lst4 = get_list_from_buffer(tst4)
    lst5 = get_list_from_buffer(tst5)
    if call.name == 'iterative':
        assert call.value(lst1) == [1, 2, 3, 5, 6, 7, 7, 13]
        assert call.value(lst2) == [1, 2, 3, 4, 5, 6, 7]
        assert call.value(lst3) == [1, 2, 3, 4, 5]
        assert call.value(lst4) == [1, 2, 3, 4, 5, 6]
        assert call.value(lst5) == [2, 2, 3, 9, 9]
    else:
        assert call.value(lst1) == ([1, 2, 3, 5, 6, 7, 7, 13], 13)
        assert call.value(lst2) == ([1, 2, 3, 4, 5, 6, 7], 21)
        assert call.value(lst3) == ([1, 2, 3, 4, 5], 1)
        assert call.value(lst4) == ([1, 2, 3, 4, 5, 6], 4)
        assert call.value(lst5) == ([2, 2, 3, 9, 9], 2)



