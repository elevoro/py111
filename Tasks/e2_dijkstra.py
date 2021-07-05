from typing import Hashable, Mapping, Union
import networkx as nx


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    g = [("A", "B", 1),
         ("B", "C", 3),
         ("C", "E", 4),
         ("E", "F", 3),
         ("B", "E", 8),
         ("C", "D", 1),
         ("D", "E", 2),
         ("B", "D", 2),
         ("G", "D", 1),
         ("D", "A", 2)]
    unvisited_nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    nodes = {node: float('inf') for node in unvisited_nodes}
    current = starting_node
    neighbor = None
    distance = 0
    nodes[current] = distance
    while len(unvisited_nodes) > 0:
        current = unvisited_nodes[0]
        for node in unvisited_nodes:
            if nodes[current] > nodes[node]:
                current = node
        for elem in g:
            if elem[0] == current or elem[1] == current:
                neighbor = elem[0]
                if neighbor == current:
                    neighbor = elem[1]
            distance = nodes[current] + elem[2]
            if distance < nodes[neighbor]:
                nodes[neighbor] = distance
        unvisited_nodes.remove(current)
    return nodes


