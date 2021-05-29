from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    first = 0
    last = len(arr) - 1
    mid = len(arr) // 2
    while arr[mid] != elem and (first < last):
        if elem > arr[mid]:
            first = mid + 1
        else:
            last = mid - 1
        mid = (first + last) // 2
    if arr[mid] != elem:
        return None
    while mid > 0 and arr[mid-1] == elem:
        mid = mid - 1
    return mid


