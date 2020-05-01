import sys


def main():
    item_list = []
    for linenum, line in enumerate(sys.stdin):
        if linenum == 0:
            item_num, capacity = line.split(' ')
        else:
            value, volume = [int(i) for i in line.split(' ')]
            item_list.append((value, volume, value/volume))
    capacity = float(capacity)
    result = 0.0
    for value, item_volume, value_per_v in sorted(item_list, key=lambda x: x[0] / x[1], reverse=True):
        if item_volume < capacity:
            result += value
            capacity -= item_volume
        else:
            result += value_per_v * capacity
            break
    print(f"{result:.3f}")
    return


if __name__ == "__main__":
    main()
