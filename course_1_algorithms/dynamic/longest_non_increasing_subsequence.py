import io
import random
import sys
from collections import deque

test1 = io.StringIO('''5
5 3 4 4 2''')

test2 = io.StringIO('''7
3 4 1 0 0 2 3''')

test3 = io.StringIO('''10
7 6 1 6 4 1 2 4 10 1''')

test4 = io.StringIO('''7
5 3 4 4 2 5 9''')

test5 = io.StringIO('''5
5 5 4 4 4''')

test6 = io.StringIO('''18
32 27 74 20 27 34 7 41 65 66 19 75 58 38 49 85 4 50''')


class BinaryIndexedTree:
    """Implementation of a Binary Indexed Tree (Fennwick Tree)"""

    def __init__(self, list):
        """"Initialize BIT with list in O(n)"""
        self.array = [0] + list
        for idx in range(1, len(self.array)):
            idx2 = idx + (idx & -idx)
            if idx2 < len(self.array):
                self.array[idx2] += self.array[idx]

    def prefix_query(self, idx):
        """Computes prefix sum of up to including the idx-th element"""
        idx += 1
        result = 0
        while idx:
            result += self.array[idx]
            idx -= idx & -idx
        return result

    def range_query(self, from_idx, to_idx):
        """Computes the range sum between two indices (both inclusive)"""
        return self.prefix_query(to_idx) - self.prefix_query(from_idx - 1)

    def update(self, idx, add):
        """Add a value to the idx-th element"""
        idx += 1
        while idx < len(self.array):
            self.array[idx] += add
            idx += idx & -idx


def restore_sequence_from_index_list(num, idx_list, prev):
    non_increasing = deque([])
    for i in range(len(idx_list)-1, -1, -1):
        if idx_list[i] == num:
            non_increasing.appendleft(i+1)
            break
    next_el = prev[i]
    while next_el >= 0:
        non_increasing.appendleft(next_el+1)
        next_el = prev[next_el]
    print(*non_increasing)
    return non_increasing


def longest_non_increasing_subsequence(str_buffer=None):
    if str_buffer:
        len_lst = int(next(str_buffer))
        lst = map(int, next(str_buffer).split(' '))
    else:
        len_lst = 20000
        lst = random.sample(range(0, 20000), 20000)
    lst = list(lst)
    subsequence_lengths = [1] * len_lst
    prev = [-1] * len_lst
    for i in range(1, len_lst):
        # j = lower_bound(lst, lst[i])
        for j in range(i):
            if lst[i] <= lst[j] and subsequence_lengths[j] + 1 >= subsequence_lengths[i]:
                subsequence_lengths[i] = subsequence_lengths[j] + 1
                prev[i] = j
    ans = max(subsequence_lengths) if len_lst else 0
    print(ans)
    ans_list = restore_sequence_from_index_list(ans, subsequence_lengths, prev)
    return ans, list(ans_list)


if __name__ == '__main__':
    assert longest_non_increasing_subsequence(test1) == (4, [1, 3, 4, 5])
    # assert longest_non_increasing_subsequence(test2) == (4, [2, 3, 4, 5])
    # assert longest_non_increasing_subsequence(test3) == (6, [1, 2, 4, 5, 8, 10])
    # assert longest_non_increasing_subsequence(test4) == (4, [1, 3, 4, 5])
    # assert longest_non_increasing_subsequence(test5) == (5, [1, 2, 3, 4, 5])
    # assert longest_non_increasing_subsequence(test6) == (5, [3, 10, 13, 15, 17])
    # longest_non_increasing_subsequence()
    