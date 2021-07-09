from typing import List
import random

def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) <= 1:
        return container

    else:
        random_elem = random.choice(container)
        left = []
        right = []
        mid = []

        for value in container:

            if value < random_elem:
                left.append(value)
            elif value > random_elem:
                right.append(value)
            else:
                mid.append(value)

    return sort(left) + mid + sort(right)
