"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any

d = {priority: [] for priority in range(11)}


def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    if priority in d:
        d[priority].append(elem)


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    for priority in d:
        if len(d[priority]) > 0:
            return d[priority].pop(0)


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    if len(d[priority]) > ind:
        return d[priority][ind]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    for priority in d:
        d[priority].clear()
