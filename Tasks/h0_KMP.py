from typing import Optional, List


def _prefix_fun(prefix_str: str) -> List[int]:
    """
    Prefix function for KMP

    :param prefix_str: dubstring for prefix function
    :return: prefix values table
    """
    prefix_list = [0]*len(prefix_str)
    for i in range(1, len(prefix_str)):
        j = prefix_list[i-1]
        while j > 0 and prefix_str[j] != prefix_str[i]:
            j = prefix_list[j-1]
        if prefix_str[j] == prefix_str[i]:
            j = j + 1
        prefix_list[i] = j
    return prefix_list


def kmp_algo(inp_string: str, substr: str) -> Optional[int]:
    """
    Implementation of Knuth-Morrison-Pratt algorithm

    :param inp_string: String where substr is to be found (haystack)
    :param substr: substr to be found in inp_string (needle)
    :return: index where first occurrence of substr in inp_string started or None if not found
    """
    ind = None
    prefix_list = _prefix_fun(substr)
    j = 0
    for i in range(len(inp_string)):
        while j > 0 and substr[j] != inp_string[i]:
            j = prefix_list[j-1]
        if substr[j] == inp_string[i]:
            j = j + 1
        if j == len(substr):
            ind = i - len(substr) + 1
            break
    return ind
