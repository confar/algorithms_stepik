import io
from functools import partial
from typing import List


class NotFound(Exception):
    pass


class ListElem:

    def __init__(self, value: str) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def __bool__(self) -> bool:
        return bool(self.head)

    def find(self, string: str) -> ListElem:
        elem = self.head
        if self.is_empty():
            raise NotFound
        while elem.value != string:
            if elem.next:
                elem = elem.next
            else:
                raise NotFound
        return elem

    def is_empty(self) -> bool:
        return not self.size

    def add(self, string: str) -> None:
        elem = ListElem(value=string)
        if not self.head:
            self.head = elem
        else:
            current_head = self.head
            self.head = elem
            self.head.next = current_head
        self.size += 1

    def remove(self, string: str) -> None:
        if self.is_empty():
            return
        elem = self.head
        if elem.value == string:
            self.head = elem.next
            self.size -= 1
        elif elem.next:
            while elem.next and elem.next.value != string:
                elem = elem.next
            if elem.next:
                removed_value_next = elem.next.next
                elem.next = removed_value_next
                self.size -= 1

    def get_values(self) -> List[str]:
        out = []
        elem = self.head
        for _ in range(self.size):
            out.append(elem.value)
            elem = elem.next
        return out


class HashTable:

    def __init__(self, size: int) -> None:
        self.array = [LinkedList() for _ in range(size)]
        self.size = size

    def add(self, string: str) -> None:
        hash = self.get_hash(string)
        lst = self.array[hash]
        try:
            lst.find(string)
        except NotFound:
            self.array[hash].add(string)

    def remove(self, string: str) -> None:
        hash = self.get_hash(string)
        lst = self.array[hash]
        lst.remove(string)

    def get_hash(self, string: str) -> int:
        return sum((ord(char) * 263 ** idx) for idx, char in enumerate(string)) % 1_000_000_007 % self.size

    def get_by_index(self, index: str) -> str:
        index = int(index)
        lst = self.array[index]
        if lst:
            return ' '.join(lst.get_values())
        return ''

    def search(self, string: str) -> str:
        hash = self.get_hash(string)
        lst = self.array[hash]
        try:
            lst.find(string)
            return 'yes'
        except NotFound:
            return 'no'


def get_method(operation, hash_table, argument):
    method_map = {
        'add': partial(hash_table.add, string=argument),
        'del': partial(hash_table.remove, string=argument),
        'find': partial(hash_table.search, string=argument),
        'check': partial(hash_table.get_by_index, index=argument)
    }
    return method_map[operation]


def main(str_buffer):
    hashmap_size = int(next(str_buffer))
    operations_count = int(next(str_buffer))
    hashtable = HashTable(hashmap_size)
    out = []
    for i in range(operations_count):
        operation, argument = next(str_buffer).split()
        func = get_method(operation, hashtable, argument)
        if operation in ('find', 'check'):
            out.append(func())
        else:
            func()
    return out


tst1 = io.StringIO('''5
12
add world
add HellO
check 4
find World
find world
del world
check 4
del HellO
add luck
add GooD
check 2
del good''')

tst2 = io.StringIO('''4
8
add test
add test
find test
del test
find test
find Test
add Test
find Test''')


tst3 = io.StringIO('''3
12
check 0
find help
add help
add del
add add
find add
find del
del del
find del
check 0
check 1
check 2''')


if __name__ == '__main__':
    assert main(tst1) == ['HellO world', 'no', 'yes', 'HellO', 'GooD luck']
    assert main(tst2) == ['yes', 'no', 'no', 'yes']
    assert main(tst3) == ['',  'no', 'yes', 'yes', 'no', '', 'add help', '']
