from typing import Hashable, Mapping, Union
import networkx as nx


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    unvisited_nodes = [node for node in g]
    nodes = {node: float('inf') for node in unvisited_nodes}
    nodes[starting_node] = 0

    while len(unvisited_nodes) > 0:
        current = unvisited_nodes[0]

        for node in unvisited_nodes:
            if nodes[current] > nodes[node]:
                current = node

        for neighbor in g[current]:
            distance = nodes[current] + g[current][neighbor]['weight']
            if distance < nodes[neighbor]:
                nodes[neighbor] = distance
        unvisited_nodes.remove(current)

    return nodes



