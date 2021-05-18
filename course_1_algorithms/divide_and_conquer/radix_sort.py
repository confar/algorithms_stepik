

def count_sort(lst, digit, radix=10):
    count_lst = [0 for _ in range(10)]
    for i in lst:
        position = int((i/radix**digit) % radix)
        count_lst[position] += 1
    for i in range(1, 10):
        count_lst[i] = count_lst[i] + count_lst[i-1]
    out = [None for _ in range(len(lst))]
    for i in lst[::-1]:
        position = int((i/radix**digit) % radix)
        out[count_lst[position]-1] = i
        count_lst[position] -= 1
    return out


def radix_sort(lst, max_digits=3):
    for i in range(0, max_digits):
        lst = count_sort(lst, digit=i)
    return lst


if __name__ == '__main__':
    assert radix_sort([1, 5, 3, 6], max_digits=1) == [1, 3, 5, 6]
    assert radix_sort([2, 3, 1, 5, 4, 8, 9, 7], max_digits=1) == [1, 2, 3, 4, 5, 7, 8, 9]
    assert radix_sort([2, 3, 9, 2, 9], max_digits=1) == [2, 2, 3, 9, 9]
    assert radix_sort([53, 89, 150, 36, 633, 233], max_digits=3) == [36, 53, 89, 150, 233, 633]
