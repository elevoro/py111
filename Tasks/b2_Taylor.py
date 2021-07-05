"""
Taylor series
"""
from typing import Union
import math


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    def current(i: int, prev: float) -> float:
        if i == 1:
            return x
        return prev * x / i
    e = 1
    pres = 0.0001
    i = 1
    item = 0
    while True:
        item = current(i, item)
        if item < pres:
            break
        e += item
        i += 1
    return e


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """

    def get_item(n: int, prev: float) -> float:
        if n == 0:
            return x
        return ((-1) ** n) * abs(prev) * x ** 2 / ((2 * n + 1) * 2 * n)
    n = 0
    result = 0
    pres = 0.0001
    current_item = 0
    while True:
        current_item = get_item(n, current_item)
        if abs(current_item) < pres:
            break
        result += current_item
        n += 1
    return result


