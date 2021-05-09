"""
Непрерывный рюкзак

Первая строка содержит количество предметов 1 < n < 10^3  и вместимость рюкзака 0 < W < 2 * 10^6. 
Каждая из следующих n строк задаёт стоимость 0 < c < 2 * 10^6 предмета
и объём 0 < w < 2 * 10^6  предмета (n, W, c, w — целые числа).

Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть,
стоимость и объём при этом пропорционально уменьшатся), помещающихся в данный рюкзак, 
с точностью не менее трёх знаков после запятой.
"""


import io

test1 = io.StringIO('''3 50
60 20
100 50
120 30''')

test2 = io.StringIO('''5 9022
3316 1601
5375 8940
2852 6912
3336 9926
1717 8427''')


def main(str_buffer):
    item_list = []
    item_num, capacity = map(int, next(str_buffer).strip().split(' '))
    capacity = float(capacity)

    for _ in range(item_num):
        value, volume = [int(i) for i in next(str_buffer).split(' ')]
        item_list.append((value, volume, value/volume))
    result = 0.0
    for value, item_volume, value_per_volume in sorted(item_list, key=lambda x: x[2], reverse=True):
        if item_volume < capacity:
            result += value
            capacity -= item_volume
        else:
            result += value_per_volume * capacity
            break
    print(f"{result:.3f}")
    return result


if __name__ == "__main__":
    assert main(test1) == 180.000
    assert main(test2) == 7777.730984340044
