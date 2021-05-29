from typing import Type, Union, Any


def fib_recursive(n: int) -> Union[Union[Type[ValueError], int], Any]:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    if n >= 2:
        return fib_recursive(n - 1) + fib_recursive(n - 2)
    else:
        return n


def fib_iterative(n: int) -> Union[Type[ValueError], int]:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    if n >= 2:
        n0, n1 = 0, 1
        for i in range(n - 1):
            n0, n1 = n1, n0 + n1
        return n1
    else:
        return n
