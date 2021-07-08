"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple

root = None


def create_node(key, value):
    return {'key': key,
            'value': value,
            'left': None,
            'right': None,
            }


def find_(key) -> Tuple[Optional[dict], Optional[dict]]:
    prev_root = None
    current_root = root
    while current_root is not None:
        if key > current_root['key']:
            prev_root = current_root
            current_root = current_root['right']

        elif key < current_root['key']:
            prev_root = current_root
            current_root = current_root['left']

        else:  # key == current_root['key']
            break

    return prev_root, current_root


def insert(key: int, value: Any) -> None:
    """
    Insert (key, value) pair to binary search tree

    :param key: key from pair (key is used for positioning node in the tree)
    :param value: value associated with key
    :return: None
    """
    global root
    prev, current = find_(key)
    if current is not None:
        current['value'] = value
    elif prev is None:
        root = create_node(key, value)
    else:
        if key > prev['key']:
            prev['right'] = create_node(key, value)
        else:  # key < prev['key']
            prev['left'] = create_node(key, value)


def remove(key: int):
    """
    Remove key and associated value from the BST if exists

    :param key: key to be removed
    :return: deleted (key, value) pair or None
    """
    prev, current = find_(key)
    if current is None: #если элемента нет
        return None
    elif prev is None:
        if current['left'] is None and current['right'] is None:#если дерево из одного листа
            clear()
        if current['left'] is None and current['right'] is not None:#если есть правый потомок
            current = current['right']
        else:
            current = current['left']

    else:
        if current['left'] is None and current['right'] is None: #если элемент это лист
            if key > prev['key']:
                prev['right'] = None
            else:  # key < prev['key']
                prev['left'] = None

        if current['left'] is None and current['right'] is not None:#если есть правый потомок
            if key > prev['key']:
                prev['right'] = current['right']
            else:  # key < prev['key']
                prev['left'] = current['left']

        if current['left'] is not None and current['right'] is None:#если есть левый потомок
            if key > prev['key']:
                prev['right'] = current['right']
            else:  # key < prev['key']
                prev['left'] = current['left']

        if current['left'] is not None and current['right'] is not None:#если есть оба потомка
            if root['left'] is not None: #нахождение самого правого в левом поддереве
                max_left = root['left']
                while max_left['right'] is not None:
                    max_left = max_left['right']
                    current['key'] = max_left['key']
                    current['value'] = max_left['value']

        return current['key'], current['value']


def find(key: int) -> Optional[Any]:
    """
    Find value by given key in the BST

    :param key: key for search in the BST
    :return: value associated with the corresponding key
    """
    _, current = find_(key)
    if current is None:
        raise KeyError(f'Key {key} not found')

    return current['value']


def clear() -> None:
    """
    Clear the tree

    :return: None
    """
    global root
    root = None
