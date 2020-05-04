import io

f = io.StringIO('''4
Insert 3
Insert 0
ExtractMax
ExtractMax''')


class Heap:
    def __init__(self):
        self.heap = []

    def __repr__(self):
        return f'{self.heap}'

    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_left_ind(self, index):
        return (2 * index) + 1

    def get_right_ind(self, index):
        return(2 * index) + 2

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def swim_up(self, cur_index):
        while self.heap[cur_index] > self.heap[self.get_parent_index(cur_index)] and cur_index != 0:
            parent_index = self.get_parent_index(cur_index)
            self.swap(cur_index, parent_index)
            cur_index = parent_index

    def sift_down(self, index):
        while self.get_left_ind(index) < len(self.heap):
            left = self.get_left_ind(index)
            right = self.get_right_ind(index)
            j = left
            if right < len(self.heap) and self.heap[right] > self.heap[left]:
                j = right
            if self.heap[index] >= self.heap[j]:
                break
            self.swap(index, j)
            index = j

    def insert(self, value):
        self.heap.append(value)
        self.swim_up(len(self.heap) - 1)

    def extract_max(self):
        if len(self.heap) == 1:
            extract = self.heap.pop()
            print(extract)
        else:
            self.swap(0, -1)
            extract = self.heap.pop()
            print(extract)
            self.sift_down(0)


def main(str_buffer):
    operation_num = int(next(str_buffer).strip())
    heap = Heap()
    for _ in range(operation_num):
        operation = next(str_buffer).strip().split(' ')
        if len(operation) == 1:
            heap.extract_max()
        else:
            operation, value = operation
            heap.insert(int(value))
    print(heap)


def test1():
    h = Heap()
    h.insert(11)
    h.insert(18)
    h.insert(22)
    assert h.heap == [22, 11, 18]
    h.insert(9)
    h.insert(8)
    assert h.heap == [22, 11, 18, 9, 8]
    h.insert(24)
    h.insert(8)
    assert h.heap == [24, 11, 22, 9, 8, 18, 8]
    h.extract_max()
    return h

if __name__ == '__main__':
    assert test1().heap == [11, 9, 22, 8, 8, 18]
    main(f)

