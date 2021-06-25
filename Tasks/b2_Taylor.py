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
    e = 0
    pres = 0.0001
    s = 1
    i = 1
    while s > pres:
        e = e + s
        s = (x ** i)/math.factorial(i)
        i = i + 1
    return e



def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    def get_item(n: int) -> float:
        return ((-1) ** n) * ((x ** (2 * n + 1)) / math.factorial(2 * n + 1))
    n = 0
    result = 0
    pres = 0.0001
    while True:
        current_item = get_item(n)
        if abs(current_item) < pres:
            break
        result += current_item
        n += 1
    return result


