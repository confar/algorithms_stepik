import io
from collections import namedtuple


class Processor(namedtuple('Processor', ['time', 'processor_num'])):
    def with_increased_time(self, new_time):
        current_time = self.time
        return self._replace(time=new_time + current_time)


class Heap:

    def __init__(self, max_size):
        self.heap = [Processor(0, i) for i in range(max_size)]
        self.max_size = max_size

    def __len__(self):
        return len(self.heap)

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
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

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

    def change_top_priority(self, new_priority):
        current_priority = self.heap[0]
        self.heap[0] = self.heap[0].with_increased_time(new_priority)
        self.sift_down(0)
        return current_priority


def main(str_buffer):
    max_size, _ = list(map(int, next(str_buffer).split()))
    tasks_lst = list(map(int, next(str_buffer).split()))
    heap = Heap(max_size)
    out = []
    for i in tasks_lst:
        task = heap.change_top_priority(i)
        out.append((task.processor_num, task.time))
    return out


tst1 = io.StringIO('''2 5\n1 2 3 4 5''')
tst2 = io.StringIO('''4 20\n1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1''')


if __name__ == '__main__':
    assert main(tst1) == [(0, 0), (1, 0), (0, 1), (1, 2), (0, 4)]
    assert main(tst2) == [(0, 0), (1, 0), (2, 0), (3, 0),
                          (0, 1), (1, 1), (2, 1), (3, 1),
                          (0, 2), (1, 2), (2, 2), (3, 2),
                          (0, 3), (1, 3), (2, 3), (3, 3),
                          (0, 4), (1, 4), (2, 4), (3, 4)]
