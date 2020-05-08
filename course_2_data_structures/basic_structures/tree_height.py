import io


def tree_height(tree_lst) -> int:
    adj_list = [[] for _ in tree_lst]
    for i, value in enumerate(tree_lst):
        if value == -1:
            root = i
            continue
        adj_list[value].append(i)
    nodes_left = [(root, adj_list[root])]
    level_counter = {root: 1}
    while nodes_left:
        parent, children = nodes_left.pop()
        for child in children:
            level_counter[child] = level_counter[parent] + 1
            sub_children = adj_list[child]
            if sub_children:
                nodes_left.append((child, sub_children))

    return max(level_counter.values())


tst1 = io.StringIO('5\n4 -1 4 1 1')
tst2 = io.StringIO('5\n-1 0 4 0 3')
tst3 = io.StringIO('10\n9 7 5 5 2 9 9 9 2 -1')


def main(str_buffer) -> int:
    next(str_buffer)
    tree_lst = [int(i) for i in next(str_buffer).split()]
    return tree_height(tree_lst)


if __name__ == '__main__':
    assert main(tst1) == 3
    assert main(tst2) == 4
    assert main(tst3) == 4
