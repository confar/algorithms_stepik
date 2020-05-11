import io
from collections import namedtuple


class Table(namedtuple('Table', ['id', 'record_count'])):
    def increase_record_count(self, delta):
        current_record_count = self.record_count
        return self._replace(record_count=current_record_count + delta)


class TableLinks:

    def __init__(self, size, table_records):
        self.set = [Table(i, table_records[i-1]) for i in range(1, size+1)]
        self.max = max(table_records)

    def swap(self, index1, index2):
        self.set[index1], self.set[index2] = self.set[index2], self.set[index1] 

    def join(self, destination, source):
        destination = self.find(destination)
        source = self.find(source)
        if destination == source:
            return self.max
        updated_destination = self.set[destination.id-1].increase_record_count(self.set[source.id-1].record_count)
        self.set[source.id-1] = updated_destination
        self.set[destination.id-1] = updated_destination
        if updated_destination.record_count > self.max:
            self.max = updated_destination.record_count
        return self.max

    def find(self, table):
        if self.set[table-1].id != table:
            self.set[table-1] = self.find(self.set[table-1].id)
        return self.set[table-1]


def main(str_buffer):
    table_count, query_count = list(map(int, next(str_buffer).split()))
    table_records = list(map(int, next(str_buffer).split()))
    tables = TableLinks(table_count, table_records)
    out = []
    for i in range(query_count):
        destination, source = list(map(int, next(str_buffer).split()))
        out.append(tables.join(destination, source))
    return out


tst1 = io.StringIO('''5 5
1 1 1 1 1
3 5
2 4
1 4
5 4
5 3''')

tst2 = io.StringIO('''6 4
10 0 5 0 3 3
6 6
6 5
5 4
4 3''')


if __name__ == '__main__':
    assert main(tst1) == [2, 2, 3, 5, 5]
    assert main(tst2) == [10, 10, 10, 11]
