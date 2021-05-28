"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any

a = []


def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    a_ = (priority, elem)
    a.append(a_)


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    if len(a) > 0:
        min_i = 0
        for i in range(len(a)):
            if a[i][0] < a[min_i][0]:
                min_i = i
        return a.pop(min_i)[1]


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    result = []
    for i in range(len(a)):
        if a[i][0] == priority:
            result.append(a[i])
    if len(result) > ind:
        return result[ind][1]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    a.clear()
