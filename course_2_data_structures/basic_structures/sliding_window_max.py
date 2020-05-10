import io

from course_2_data_structures.basic_structures.stack_max import MaxStack, StackValue


class Queue:

    def __init__(self, max_size):
        self.max_size = max_size
        self.current_size = 0
        self.to_push = MaxStack()
        self.to_pop = MaxStack()

    def push_back(self, value):
        if self.to_push.is_empty():
            self.to_push.push(value)
        else:
            maximum = max(self.to_push.max(), value)
            self.to_push.array.append(StackValue(value, maximum=maximum))
        self.current_size += 1

    def pop_front(self):
        if self.to_pop.is_empty():
            while not self.to_push.is_empty():
                elem = self.to_push.pop()
                if not self.to_pop.is_empty():
                    maximum = max(self.to_pop.max(), elem)
                else:
                    maximum = elem
                self.to_pop.array.append(StackValue(elem, maximum))
        self.to_pop.pop()
        self.current_size -= 1

    def __str__(self) -> str:
        return f'Queue size {self.max_size} push {self.to_push} pop {self.to_pop.array}'

    __repr__ = __str__

    def get_max(self):
        if self.to_push.is_empty():
            maximum = self.to_pop.max()
        elif self.to_pop.is_empty():
            maximum = self.to_push.max()
        else:
            maximum = max(self.to_pop.max(), self.to_push.max())
        return maximum


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

tst8 = io.StringIO('''15
27 83 29 77 6 3 48 2 16 72 46 38 55 2 58
5''')

tst9 = io.StringIO('''3
2 1 5
2''')


def main(str_buffer):
    (next(str_buffer))
    num_lst = list(map(int, next(str_buffer).split()))
    max_size = int(next(str_buffer))
    queue = Queue(max_size=max_size)
    out = []
    for index, value in enumerate(num_lst):
        queue.push_back(value)
        if queue.current_size >= max_size:
            out.append(queue.get_max())
            queue.pop_front()
    return out


if __name__ == '__main__':
    assert main(tst1) == [7, 7, 5, 6, 6]
    assert main(tst2) == [2, 1, 5]
    assert main(tst3) == [9]
    assert main(tst4) == [73, 97, 97, 97, 97, 97, 97, 97, 42]
    assert main(tst5) == [93, 93, 93, 93]
    assert main(tst6) == [79, 79, 79, 79]
    assert main(tst7) == [61, 90, 90, 90, 84, 84, 25, 25, 25, 78, 78, 78, 47]
    assert main(tst8) == [83, 83, 77, 77, 48, 72, 72, 72, 72, 72, 58]
    assert main(tst9) == [2, 5]
