import io


class QueueElem:

    def __init__(self, index, value):
        self.index = index
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return f'{self.index} value: {self.value}'

    __repr__ = __str__


class Queue:

    def __init__(self, max_size):
        self.max_size = max_size
        self.current_size = 0
        self.head = None
        self.tail = None
        self.max = None
        self.second_max = None

    def push_back(self, elem):
        if not self.head and not self.tail:
            self.head = elem
            self.tail = elem
        else:
            current_tail = self.tail
            current_tail.next = elem
            self.tail = elem
            if self.max and self.tail.value >= self.max:
                self.second_max = self.max
                self.max = self.tail.value
            elif self.max and self.tail.value > self.second_max:
                self.second_max = elem.value
        self.current_size += 1

    def pop_front(self):
        current_head = self.head
        if self.max == current_head.value:
            self.max = self.second_max
        elif self.second_max == current_head.value:
            self.second_max = 0
        next_head = current_head.next
        self.head = next_head
        self.current_size -= 1
        if self.current_size == 0:
            self.head = self.tail = self.max = None

    def __str__(self) -> str:
        return f'Queue size {self.max_size} head {self.head} tail {self.tail}'

    __repr__ = __str__

    def get_max(self):
        if self.max_size == 1:
            return self.head.value
        if not self.max:
            if self.head.value > self.head.next.value:
                maximum = self.head.value
                second_maximum = self.head.next.value
            else:
                maximum = self.head.next.value
                second_maximum = self.head.value
            elem = self.head.next.next
            for _ in range(self.max_size-2):
                if elem.value >= maximum:
                    second_maximum = maximum
                    maximum = elem.value
                elif elem.value > second_maximum:
                    second_maximum = elem.value
                elem = elem.next
            self.max = maximum
            self.second_max = second_maximum
        return self.max


tst1 = io.StringIO('''8
2 7 3 1 5 2 6 2
4''')

tst2 = io.StringIO('''3
2 1 5
1''')

tst3 = io.StringIO('''3
2 3 9
3''')

tst4 = io.StringIO('''15
73 65 24 14 44 20 65 97 27 6 42 1 6 41 16
7''')

tst5 = io.StringIO('''15
28 7 64 40 68 86 80 93 4 53 32 56 68 18 59
12''')

tst6 = io.StringIO('''15
16 79 20 19 43 72 78 33 40 52 70 79 66 43 60
12''')

tst7 = io.StringIO('''15
34 51 61 90 26 84 2 25 7 8 25 78 21 47 25
3''')


def main(str_buffer):
    (next(str_buffer))
    num_lst = list(map(int, next(str_buffer).split()))
    max_size = int(next(str_buffer))
    queue = Queue(max_size=max_size)
    out = []
    for index, value in enumerate(num_lst):
        queue.push_back(QueueElem(index=index, value=value))
        if queue.current_size >= max_size:
            out.append(queue.get_max())
            queue.pop_front()
    return out
    #return ' '.join(map(str, out))


if __name__ == '__main__':
    # assert main(tst1) == [7, 7, 5, 6, 6]
    # assert main(tst2) == [2, 1, 5]
    # assert main(tst3) == [9]
    # assert main(tst4) == [73, 97, 97, 97, 97, 97, 97, 97, 42]
    # assert main(tst5) == [93, 93, 93, 93]
    # assert main(tst6) == [79, 79, 79, 79]
    result = main(tst7) 
    assert result == [61, 90, 90, 90, 84, 84, 25, 25, 25, 78, 78, 78, 47]
