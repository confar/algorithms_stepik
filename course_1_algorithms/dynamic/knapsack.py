def knapsack(capacity, number_of_items, item_weights, item_values=None):
    knapsack = [[0 for _ in range(capacity + 1)] for _ in range(number_of_items + 1)]
    if not item_values:
        item_values = item_weights[:]
    for item_idx in range(1, number_of_items+1):
        for weight_limit in range(1, capacity+1):
            item_weight = item_weights[item_idx - 1]
            item_value = item_values[item_idx - 1]
            left_capacity = weight_limit - item_weight
            if left_capacity >= 0:
                knapsack[item_idx][weight_limit] = max(knapsack[item_idx-1][weight_limit],
                                                       item_value + knapsack[item_idx-1][left_capacity])
            else:
                knapsack[item_idx][weight_limit] = knapsack[item_idx-1][weight_limit]
    result = knapsack[number_of_items][capacity]
    print(result)
    return result


if __name__ == '__main__':
    assert knapsack(capacity=12, number_of_items=5, item_weights=[7, 3, 1, 5, 4], item_values=[10, 4, 2, 6, 7]) == 19
    assert knapsack(capacity=5, number_of_items=4, item_weights=[5, 3, 4, 2], item_values=[60, 50, 70, 30]) == 80
    assert knapsack(capacity=4, number_of_items=3, item_weights=[1, 3, 8]) == 4
    assert knapsack(capacity=10, number_of_items=3, item_weights=[1, 4, 8]) == 9
