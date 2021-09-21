import io


class WrongInequality(Exception):
    pass


class SystemEquations:
    def __init__(self, size):
        self.lst = [i for i in range(1, size+1)]

    def check_equality(self, var1, var2):
        destination = self.find(var1)
        source = self.find(var2)
        if destination == source:
            return
        self.lst[var2-1] = var1

    def check_inequality(self, var1, var2):
        destination = self.find(var1)
        source = self.find(var2)
        if destination == source:
            raise WrongInequality

    def find(self, var):
        if self.lst[var-1] != var:
            self.lst[var-1] = self.find(self.lst[var-1])
        return self.lst[var-1]


def main(str_buffer):
    var_count, equality_count, inequality_count = map(int, next(str_buffer).split())
    system = SystemEquations(var_count)
    out = []
    for i in range(equality_count):
        var1, var2 = map(int, next(str_buffer).split())
        out.append(system.check_equality(var1, var2))
    for i in range(inequality_count):
        var1, var2 = map(int, next(str_buffer).split())
        try:
            out.append(system.check_inequality(var1, var2))
        except WrongInequality:
            return 0
    return 1


tst1 = io.StringIO('''4 6 0
1 2
1 3
1 4
2 3
2 4
3 4''')

tst2 = io.StringIO('''6 5 3
2 3
1 5
2 5
3 4
4 2
6 1
4 6
4 5''')


if __name__ == '__main__':
    assert main(tst1) == 1
    assert main(tst2) == 0
