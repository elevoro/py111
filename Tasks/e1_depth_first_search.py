from typing import Hashable, List
import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    visited = {start_node}
    stack = []
    sorted_node = [start_node]
    for neighbor in g.neighbors(start_node):
        stack.append(neighbor)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            sorted_node.append(node)
            for neighbor in g.neighbors(node):
                if neighbor not in visited:
                    stack.append(neighbor)

    return sorted_node



