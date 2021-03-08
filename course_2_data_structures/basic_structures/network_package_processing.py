import io
from typing import List, Optional


class Package:

    def __init__(self, index, arrival, duration):
        self.index = index
        self.arrival = arrival
        self.duration = duration
        self.start = None
        self.end = None

    def is_successor(self, other):
        return bool((self.arrival + self.duration) - (other.arrival + other.duration))

    def __str__(self) -> str:
        return f'Package: arrival: {self.arrival}, duration: {self.duration}, start: {self.start}, end: {self.end}'

    __repr__ = __str__


class QueueEmpty(Exception):
    pass


class QueueFull(Exception):
    pass


class Queue:
    __slots__ = ['array', 'max_index', 'head', 'tail', 'size', 'max_size']

    def __init__(self, max_size) -> None:
        self.array: List[Optional[Package]] = [None for _ in range(max_size)]
        self.max_index = max_size - 1
        self.size = 0
        self.max_size = max_size
        self.head = 0
        self.tail = 0

    def __str__(self) -> str:
        return f'Queue: {self.array}'

    __repr__ = __str__

    def enqueue(self, package):
        if self.is_full():
            raise QueueFull()
        self.array[self.tail] = package
        self.tail = int((self.tail + 1) % self.max_size)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise QueueEmpty()
        first = self.array[self.head]
        self.head = int((self.head + 1) % self.max_size)
        self.size -= 1
        return first

    def front(self) -> Package:
        if not self.is_empty():
            return self.array[self.head]
        raise QueueEmpty()

    def back(self) -> Package:
        if not self.is_empty():
            return self.array[self.tail-1]
        raise QueueEmpty()

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size


class NetworkBuffer:

    def __init__(self, size):
        self.queue = Queue(size)
        self.size = size
        self.min_free_time = 0

    def store_and_process(self, package: Package):
        if not self.queue.is_full():
            package.start = max(self.min_free_time, package.arrival)
            package.end = package.start + package.duration
            self.min_free_time = package.end
            self.queue.enqueue(package)
        else:
            if package.arrival >= self.queue.front().end:
                self.queue.dequeue()
                package.start = max(self.min_free_time, package.arrival)
                package.end = package.start + package.duration
                self.min_free_time = package.end
                self.queue.enqueue(package)
            else:
                return -1
        return package.start

    def __str__(self) -> str:
        return f'Network buffer: queue {self.queue}'

    __repr__ = __str__


def main(str_buffer):
    queue_size, package_num = map(int, next(str_buffer).split())
    if not package_num:
        return '\n'
    queue = NetworkBuffer(queue_size)
    out = []
    for index in range(package_num):
        arrival, duration = map(int, next(str_buffer).split())
        package = Package(index=index, arrival=arrival, duration=duration)
        out.append(queue.store_and_process(package))
    return '\n'.join(map(str, out))


tst1 = io.StringIO(f'1 0')
tst2 = io.StringIO(f'1 1\n'
                   f'0 0')
tst3 = io.StringIO(f'1 2\n'
                   f'0 1\n'
                   f'0 1')
tst4 = io.StringIO(f'1 2\n'
                   f'0 1\n'
                   f'1 1')

tst6 = io.StringIO(f'''1 25
16 0
29 3
44 6
58 0
72 2
88 8
95 7
108 6
123 9
139 6
152 6
157 3
169 3
183 1
192 0
202 8
213 8
229 3
232 3
236 3
239 4
247 8
251 2
267 7
275 7''')

tst7 = io.StringIO('''2 4
0 0
1 0
1 1
1 2''')

tst8 = io.StringIO('''2 8
0 0
0 0
0 0
1 0
1 0
1 1
1 2
1 3''')

tst9 = io.StringIO('''2 5
1 1
1 0
1 0
1 2
1 3''')

tst10 = io.StringIO('''1 5
999999 1
1000000 0
1000000 1
1000000 0
1000000 0''')

tst11 = io.StringIO('''2 5
2 9
4 8
10 9
15 2
19 1''')




if __name__ == '__main__':
    assert main(tst1) == '\n'
    assert main(tst2) == '0'
    assert main(tst3) == '0\n-1'
    assert main(tst4) == '0\n1'
    result = main(tst6)
    assert result == '\n'.join(map(str, [16, 29, 44, 58, 72, 88, -1, 108, 123, 139, 152, -1,
                                         169, 183, 192, 202, 213, 229, 232, 236, 239, 247, -1, 267, 275]))
    assert main(tst8) == '\n'.join(map(str, [0, 0, 0, 1, 1, 1, 2, -1]))
    result = main(tst9)
    assert result == '\n'.join(map(str, [1, 2, -1, -1, -1]))
    assert main(tst10) == '\n'.join(map(str, [999999, 1000000, 1000000, -1, -1]))
    result = main(tst11)
    assert result == '\n'.join(map(str, [2, 11, -1, 19, 21]))
