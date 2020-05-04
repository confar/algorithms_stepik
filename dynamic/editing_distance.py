import math


def diff(char1, char2):
    return 1 if char1 != char2 else 0


def _edit_distance(distance, i, j, str1, str2):
    if distance[i][j] == math.inf:
        if i == 0:
            distance[i][j] = j
        elif j == 0:
            distance[i][j] = i
        else:
            insert = _edit_distance(distance, i, j - 1, str1, str2) + 1
            delete = _edit_distance(distance, i - 1, j, str1, str2) + 1
            substitute = _edit_distance(distance, i - 1, j - 1, str1, str2) + diff(str1[i-1], str2[j-1])
            distance[i][j] = min(insert, delete, substitute)
    return distance[i][j]


def edit_distance(str1, str2):
    rows = len(str1) + 1
    cols = len(str2) + 1
    distance = [[math.inf for _ in range(cols)] for _ in range(rows)]
    for i in range(1, rows):
        for k in range(1, cols):
            distance[i][0] = i
            distance[0][k] = k

    for i in range(rows):
        for j in range(cols):
            _edit_distance(distance, i, j, str1, str2)
    result = distance[len(str1)][len(str2)]
    print(result)
    return result


if __name__ == '__main__':
    assert edit_distance('ab', 'ab') == 0
    assert edit_distance('short', 'ports') == 3
    assert edit_distance('editing', 'distance') == 5

