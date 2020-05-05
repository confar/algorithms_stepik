import math
from collections import deque


def calculate_steps_from_number_to_one(number):
    operation_list = deque([number])
    step_list = [0] + [math.inf for _ in range(number)]
    prev_list = [math.inf for _ in range(number)]
    if number != 1:
        for num in range(1, number):
            for value in (num * 3, num * 2, num + 1):
                if value <= number and step_list[num - 1] + 1 < step_list[value - 1]:
                    step_list[value - 1] = step_list[num - 1] + 1
                    prev_list[value - 1] = num
    while number > 1:
        new_elem = prev_list[number-1]
        operation_list.appendleft(new_elem)
        number = new_elem
    return len(operation_list) - 1, list(operation_list)


def main():
    assert calculate_steps_from_number_to_one(1) == (0, [1])
    assert calculate_steps_from_number_to_one(5) == (3, [1, 2, 4, 5])
    assert (calculate_steps_from_number_to_one(96234) == (
        14, [1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234]))


if __name__ == '__main__':
    main()
