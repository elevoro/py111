from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    n = 1
    while n < len(container):
        for i in range(len(container) - n):
            if container[i] > container[i + 1]:
                container[i], container[i + 1] = container[i + 1], container[i]
        n += 1
    return container
