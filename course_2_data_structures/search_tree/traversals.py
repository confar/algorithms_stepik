import io


class Tree:

    def __init__(self, size):
        self.array = [None for _ in range(size)]
        self.in_order_out = []
        self.pre_order_out = []
        self.post_order_out = []

    def get_node(self, index):
        if index == -1:
            return
        return self.array[index]

    def pre_order_traverse(self, node):
        if not node:
            return
        self.pre_order_out.append(node.val)
        self.pre_order_traverse(self.get_node(node.left))
        self.pre_order_traverse(self.get_node(node.right))

    def post_order_traverse(self, node):
        if not node:
            return
        self.post_order_traverse(self.get_node(node.left))
        self.post_order_traverse(self.get_node(node.right))
        self.post_order_out.append(node.val)

    def in_order_traverse(self, node):
        if not node:
            return
        self.in_order_traverse(self.get_node(node.left))
        self.in_order_out.append(node.val)
        self.in_order_traverse(self.get_node(node.right))


class Node:

    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def main(str_buffer):
    tree_size = int(next(str_buffer))
    tree = Tree(tree_size)
    out = []
    for i in range(tree_size):
        node_value, left, right = map(int, next(str_buffer).split())
        tree.array[i] = Node(val=node_value, left=left, right=right)
    tree.in_order_traverse(tree.array[0])
    tree.pre_order_traverse(tree.array[0])
    tree.post_order_traverse(tree.array[0])
    for lst in (tree.in_order_out, tree.pre_order_out, tree.post_order_out):
        print_traversal(lst)
    return out


def print_traversal(lst):
    print(' '.join(map(str, lst)))


tst1 = io.StringIO('''5
4 1 2
2 3 4
5 -1 -1
1 -1 -1
3 -1 -1''')


if __name__ == '__main__':
    main(tst1)
