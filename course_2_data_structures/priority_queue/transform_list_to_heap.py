import io
import math


class Heap:

    def __init__(self, max_size):
        self.heap = []
        self.max_size = max_size
        self.change_count = 0
        self.log = []

    def __len__(self):
        return len(self.heap)

    @classmethod
    def build_from_list(cls, lst, size):
        heap = cls(size)
        heap.heap = lst
        for i in range((size // 2 - 1), -1, -1):
            heap.sift_down(i)
        return heap.change_count, heap.log

    @staticmethod
    def parent_index(index):
        return (index - 1) // 2

    @staticmethod
    def left_child_index(index):
        return index * 2 + 1

    @staticmethod
    def right_child_index(index):
        return index * 2 + 2

    def swap(self, index1, index2):
        self.change_count += 1
        self.log.append((index1, index2))
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def swim_up(self, index):
        out = []
        parent_index = self.parent_index(index)
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            self.swap(index, parent_index)
            out.append((parent_index, index))
            index = parent_index
            parent_index = self.parent_index(parent_index)
        return out

    def sift_down(self, index):
        min_index = index
        left_child = self.left_child_index(index)
        if left_child <= self.max_size-1 and self.heap[left_child] < self.heap[min_index]:
            min_index = left_child
        right_child = self.right_child_index(index)
        if right_child <= self.max_size-1 and self.heap[right_child] < self.heap[min_index]:
            min_index = right_child
        if index != min_index:
            self.swap(index, min_index)
            self.sift_down(min_index)

    def extract_max(self):
        minimum = self.heap[0]
        self.swap(0, -1)
        self.sift_down(0)
        return minimum

    def change_priority(self, index, new_priority):
        current_priority = self.heap[index]
        self.heap[index] = current_priority
        if new_priority > current_priority:
            self.sift_down(index)
        else:
            self.swim_up(index)

    def remove(self, index):
        self.change_priority(index, math.inf)
        self.extract_max()

    def insert(self, value):
        self.heap.append(value)
        self.swim_up(-1)


def main(str_buffer):
    size = int(next(str_buffer))
    num_lst = list(map(int, next(str_buffer).split()))
    swap_count, swap_indexes_log = Heap.build_from_list(num_lst, size)
    return swap_count, swap_indexes_log


tst1 = io.StringIO('''5\n5 4 3 2 1''')
tst2 = io.StringIO('''5\n1 2 3 4 5''')
tst3 = io.StringIO('''6\n7 6 5 4 3 2''')


if __name__ == '__main__':
    assert main(tst1) == (3, [(1, 4), (0, 1), (1, 3)])
    assert main(tst2) == (0, [])
    assert main(tst3) == (4, [(2, 5), (1, 4), (0, 2), (2, 5)])
