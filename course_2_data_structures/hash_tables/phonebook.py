import io


class NotFound(Exception):
    pass


class ListElem:

    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def find(self, value):
        elem = self.head
        if self.is_empty():
            raise NotFound
        while elem.number != value:
            if elem.next:
                elem = elem.next
            else:
                raise NotFound
        return elem

    def is_empty(self):
        return not self.size

    def add(self, elem):
        if not self.head:
            self.head = elem
        else:
            current_head = self.head
            self.head = elem
            self.head.next = current_head
        self.size += 1

    def remove(self, phone):
        if self.is_empty():
            return
        elem = self.head
        if elem.number == phone:
            self.head = elem.next
            self.size -= 1
        elif elem.next:
            while elem.next and elem.next.number != phone:
                elem = elem.next
            if elem.next:
                removed_value_next = elem.next.next
                elem.next = removed_value_next
                self.size -= 1


class HashTable:

    def __init__(self, size):
        self.array = [LinkedList() for _ in range(size)]
        self.size = size

    def add(self, phone, name):
        hash = self.get_hash(phone)
        lst = self.array[hash]
        try:
            value_exists = lst.find(phone)
            value_exists.name = name
        except NotFound:
            self.array[hash].add(ListElem(name=name, number=phone))

    def remove(self, phone):
        hash = self.get_hash(phone)
        lst = self.array[hash]
        lst.remove(phone)

    def get_hash(self, phone_num):
        return phone_num % self.size

    def search(self, phone):
        hash = self.get_hash(phone)
        lst = self.array[hash]
        try:
            return lst.find(phone).name
        except NotFound:
            return 'not found'


def main(str_buffer):
    operations_count = int(next(str_buffer))
    phonebook = HashTable(operations_count)
    out = []
    for i in range(operations_count):
        operation_statement = next(str_buffer).split()
        if len(operation_statement) == 3:
            _, number, name = operation_statement
            phonebook.add(int(number), name)
        else:
            operation, number = operation_statement
            if operation == 'find':
                out.append(phonebook.search(int(number)))
            else:
                phonebook.remove(int(number))
    return out


tst1 = io.StringIO('''12
add 911 police
add 76213 Mom
add 17239 Bob
find 76213
find 910
find 911
del 910
del 911
find 911
find 76213
add 76213 daddy
find 76213''')

tst2 = io.StringIO('''8
find 3839442
add 123456 me
add 0 granny
find 0
find 123456
del 0
del 0
find 0''')


if __name__ == '__main__':
    assert main(tst1) == ['Mom', 'not found', 'police', 'not found', 'Mom', 'daddy']
    assert main(tst2) == ['not found', 'granny', 'me', 'not found']
