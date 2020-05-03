import io

f = io.StringIO('''8
Insert 200
Insert 10
Insert 5
Insert 500
ExtractMax
ExtractMax
ExtractMax
ExtractMax''')


class Heap:
    def __init__(self):
        self.heap = []

    def __repr__(self):
        return f'{self.heap}'

    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_children_indexes(self, index):
        return (2 * index) + 1, (2 * index) + 2

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def swim_up(self, cur_index):
        while self.heap[cur_index] < self.heap[self.get_parent_index(cur_index)] and cur_index != 0:
            parent_index = self.get_parent_index(cur_index)
            self.swap(cur_index, parent_index)
            cur_index = parent_index

    def sift_down(self, cur_index):
        while self.heap[cur_index] < self.heap[self.get_parent_index(cur_index)] and cur_index != 0:
            parent_index = self.get_parent_index(cur_index)
            self.swap(cur_index, parent_index)
            cur_index = parent_index

    def insert(self, value):
        self.heap.append(value)
        self.swim_up(len(self.heap) - 1)

    def get_max(self):
        return self.heap.pop(0)


def main(str_buffer):
    operation_num = int(next(str_buffer).strip())
    heap = Heap()
    for _ in range(operation_num):
        operation = next(str_buffer).strip().split(' ')
        if len(operation) == 1:
            print(heap.get_max())
        else:
            operation, value = operation
            heap.insert(int(value))

main(f)