from itertools import islice
from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    cost0 = stairway[0]
    cost1 = stairway[1]
    for cost in islice(stairway, 2, len(stairway)):
        current = cost + min(cost1, cost0)
        cost0, cost1 = cost1, current
    return cost1
