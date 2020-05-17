import io


class IncorrentTree(Exception):
    pass


class Tree:
    def __init__(self, size):
        self.array = [None for _ in range(size)]
        self.size = size
        self.out = []

    def add(self, value, left, right):
        self.array.append(Node(value, left, right))

    def get_node(self, index):
        if index == -1:
            return
        return self.array[index]

    def postorder_traversal(self, node=None):
        if not node:
            return
        self.postorder_traversal(self.get_node(node.left))
        self.postorder_traversal(self.get_node(node.right))
        if self.out and self.out[-1] > node.value:
            raise IncorrentTree
        self.out.append(node.value)


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.value} left: {self.left}, right: {self.right}'


def main(str_buffer):
    tree_size = int(next(str_buffer))
    if not tree_size:
        return 'CORRECT'
    tree = Tree(tree_size)
    for i in range(tree_size):
        node_value, left, right = map(int, next(str_buffer).split())
        tree.array[i] = Node(value=node_value, left=left, right=right)
    try:
        tree.postorder_traversal(tree.array[0])
        return 'CORRECT'
    except IncorrentTree:
        return 'INCORRECT'


if __name__ == '__main__':
    tst1 = io.StringIO('''3
    2 1 2
    1 -1 -1
    3 -1 -1''')
    assert main(tst1) == 'CORRECT'

    tst2 = io.StringIO('''3
        1 1 2
        2 -1 -1
        3 -1 -1''')
    assert main(tst2) == 'INCORRECT'

    tst3 = io.StringIO('''3
    2 1 2
    1 -1 -1
    2 -1 -1''')
    assert main(tst3) == 'CORRECT'

    tst4 = io.StringIO('''3
    2 1 2
    2 -1 -1
    3 -1 -1''')
    assert main(tst4) == 'INCORRECT'

    tst5 = io.StringIO('''1
        2147483647 -1 -1''')
    assert main(tst5) == 'CORRECT'

    tst6 = io.StringIO('''5
        1 -1 1
        2 -1 2
        3 -1 3
        4 -1 4
        5 -1 -1''')
    assert main(tst6) == 'CORRECT'

    tst7 = io.StringIO('''7
        4 1 2
        2 3 4
        6 5 6
        1 -1 -1
        3 -1 -1
        5 -1 -1
        7 -1 -1''')
    assert main(tst7) == 'CORRECT'



def convert_to_16(str1):
    nums = map(int, list(str1))
    for i, val in reversed(enumerate(nums)):
        print(i, val)
