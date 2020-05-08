import io

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


class Package:

    def __init__(self, index, arrival, duration):
        self.index = index
        self.arrival = arrival
        self.duration = duration

    def is_successor(self, other):
        return bool((self.arrival + self.duration) - (other.arrival + other.duration))

    def __str__(self) -> str:
        return (f'Package: arrival: {self.arrival} duration: {self.duration}')

    __repr__ = __str__


class NetworkBuffer:

    def __init__(self, size):
        self.queue = [None for _ in range(size)]
        self.size = size
        self.head = None
        self.tail = None

    def store_and_process(self, elem):
        if self.head and self.tail and self.tail - self.head + 1 > self.size:
            return -1
        if not self.head and not self.tail:
            self.head = self.tail = 0
        self.queue[self.tail] = elem
        self.tail += 1
        return self.process()

    def process(self):
        first_package = self.queue[self.head]
        self.queue[self.head] = None
        return first_package.duration

    def __str__(self) -> str:
        return (f'Network buffer: queue {self.queue}')

    __repr__ = __str__


def main(str_buffer):
    queue_size, package_num = map(int, next(str_buffer).split())
    if not package_num:
        return None
    queue = NetworkBuffer(queue_size)
    out = []
    for index in range(package_num):
        arrival, duration = map(int, next(str_buffer).split())
        package = Package(index=index, arrival=arrival, duration=duration)
        out.append(queue.store_and_process(package))
    return '\n'.join(map(str, out))


tst1 = io.StringIO(f'1 0')
tst2 = io.StringIO(f'1 1\n0 0')
tst3 = io.StringIO(f'1 2\n0 1\n0 1')
tst4 = io.StringIO(f'1 2\n0 1\n1 1')
tst5 = io.StringIO(f'''2 8
0 0
0 0
0 0
1 0
1 0
1 1
1 2
1 3''')

if __name__ == '__main__':
    # assert main(tst1) is None
    # assert main(tst2) == '0'
    assert main(tst3) == '0\n-1'
    assert main(tst4) == '0\n1'
    result = main(tst5) 
    assert result == '0\n0\n0\n1\n1\n1\n2\n-1'
    result = main(tst6)
    assert result == '16 29 44 58 72 88 -1 108 123 139 152 -1 169 183 192 202 213 229 232 236 239 247 -1 267 275'

