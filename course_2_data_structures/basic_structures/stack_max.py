import io
from collections import namedtuple
from typing import List


class EmptyStack(Exception):
    pass


StackValue = namedtuple('StackValue', ['value', 'maximum'])


class MaxStack:
    __slots__ = ['array', 'max_array']

    def __init__(self) -> None:
        self.array: List[StackValue] = []

    def pop(self) -> int:
        if not self.is_empty():
            return self.array.pop().value
        raise EmptyStack

    def top(self) -> StackValue:
        if not self.is_empty():
            return self.array[-1]
        raise EmptyStack

    def is_empty(self) -> bool:
        return not self.array

    def max(self) -> int:
        if not self.is_empty():
            return self.array[-1].maximum
        raise EmptyStack

    def push(self, value: int) -> None:
        if self.is_empty():
            maximum = value
        else:
            maximum = max(self.max(), value)
        self.array.append(StackValue(value, maximum))


def main(str_buffer):
    operation_num = int(next(str_buffer))
    stack = MaxStack()
    out = []
    for _ in range(operation_num):
        operation = next(str_buffer).split()
        func = getattr(stack, operation[0])
        if len(operation) > 1:
            func(int(operation[-1]))
        elif operation[0] == 'max':
            out.append(func())
        else:
            func()
    return '\n'.join(map(str, out))


tst1 = io.StringIO('''5
push 2
push 1
max
pop
max''')

tst2 = io.StringIO('''5
push 1
push 2
max
pop
max''')

tst3 = io.StringIO('''10
push 2
push 3
push 9
push 7
push 2
max
max
max
pop
max''')

if __name__ == '__main__':
    assert main(tst1) == '2\n2'
    assert main(tst2) == '2\n1'
    assert main(tst3) == '9\n9\n9\n9'
