from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence, start = 0, end = None) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if end is None:
        end = len(arr) - 1
    if start > end:
        return None
    mid = (start + end) // 2
    if elem == arr[mid]:
        return mid
    while mid > 0 and arr[mid-1] == elem:
        mid = mid - 1
    if elem < arr[mid]:
        return binary_search(elem, arr, start, mid-1)
    if elem > arr[mid]:
        return binary_search(elem, arr, mid+1, end)


