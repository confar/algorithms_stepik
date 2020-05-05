import time


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
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


if __name__ == '__main__':
    assert fib_recursive(4) == 3
    assert fib_recursive(5) == 5
    assert fib_recursive(6) == 8
