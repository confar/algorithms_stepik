
def memo(func):
    cache = {}

    def wrapper(n):
        if n in cache:
            print(f'returned {n} from cache')
            return cache[n]
        result = func(n)
        cache[n] = result
        print(f'calculated result for {n} = {result}')
        return result
    return wrapper


@memo
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_recursion(n):
    if n <= 1:
        return n
    return fib_recursion(n - 1) + fib_recursion(n - 2)


def fib_recursive_top_down(n, dp_array=None):
    if dp_array is None:
        dp_array = [None for _ in range(n+1)]
    if dp_array[n] is None:
        if n <= 1:
            dp_array[n] = n
        else:
            dp_array[n] = fib_recursive_top_down(n - 1, dp_array) + fib_recursive_top_down(n - 2, dp_array)
    return dp_array[n]


def fib_iterative_bottom_up(n):
    dp_array = [-1 for _ in range(n+1)]
    dp_array[0] = 0
    dp_array[1] = 1
    for i in range(2, n+1):
        dp_array[i] = dp_array[i-1] + dp_array[i-2]
    return dp_array[n]


if __name__ == '__main__':
    assert fib_recursive(4) == 3
    assert fib_recursive(5) == 5
    assert fib_recursive(6) == 8
    assert fib_recursive(40) == 102334155
    assert fib_recursive_top_down(4) == 3
    assert fib_recursive_top_down(5) == 5
    assert fib_recursive_top_down(6) == 8
    assert fib_recursive_top_down(40) == 102334155
    assert fib_iterative_bottom_up(4) == 3
    assert fib_iterative_bottom_up(5) == 5
    assert fib_iterative_bottom_up(6) == 8
    assert fib_iterative_bottom_up(40) == 102334155
