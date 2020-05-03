import io


def binary_search(value, search_list):
    start = 1
    end = len(search_list)
    while start <= end:
        middle = (start + end) // 2
        lst_value = search_list[middle-1]
        if lst_value == value:
            return middle
        elif lst_value > value:
            end = middle - 1
        else:
            start = middle + 1
    return -1


def main(str_buffer):
    _, *search_list = [int(i) for i in next(str_buffer).strip().split(' ')]
    _, *input_list = [int(i) for i in next(str_buffer).strip().split(' ')]
    output_list = []
    for i in input_list:
        found_index = binary_search(i, search_list)
        output_list.append(found_index)
    print(' '.join(map(str, output_list)))
    return output_list


tst1 = io.StringIO(f'''5 1 5 8 12 13
                   5 8 1 23 1 11''')

if __name__ == '__main__':
    assert main(tst1) == [3, 1, -1, 1, -1]
