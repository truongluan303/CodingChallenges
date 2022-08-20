from collections import deque
from dataclasses import dataclass
from pprint import pprint
from random import randint
from typing import List, Optional


"""
This is a 2-part question.
---

The first part is to generate a matrix of nodes in a network,
where one node is a gateway.

    The rule to generate the network of nodes is actually simple.

    * You can assign the node ID to any number you want as long as
        you can make sure there are no duplicates.

    * The `x` and `y` coordinates can be generated with a random
        number in range [0, num_nodes * 2). It is ok to have 2 nodes
        at the same location.

    * The gateway is selected randomly among all the nodes (all nodes
        must have the same chance of being a gateway). The node that
        is chosen to be the gateway will have the `is_gw` flag set.

You will have to implement method `create_nodes` for this task.

---

The second part is to find all the nodes that are connected to the
gateway. A connection between 2 nodes is formed if the distance
between those 2 nodes is not bigger than `dislimit`. A node is connected
to the gateway if there is a connection from itself to the gateway, or
if if it is connected a node that is directly or not directly connected
to the gateway.

For example, if G is the gateway, and the `dislimit` is 4, then there will
be 4 nodes connected to G in this example below: [1, 2, 3]

        1 * * * G * * * * * * 4
        * * * * * * * * * * * 5
        * * * * * * * 6 * * * *
        2 * 3 * * * * * * * * *
    
You will have to implement method `get_connected_nodes` for this task.
"""


@dataclass
class Node:
    id: Optional[int] = None
    x: Optional[int] = None
    y: Optional[int] = None
    is_gw: Optional[bool] = None


def get_distance(node1: Node, node2: Node):
    return abs(node1.x - node2.x) + abs(node1.y - node2.y)


def print_nodes(nodes: List[Node]) -> None:
    """
    Print a matrix of nodes in the network, where gateway is highlighted.
    """
    [print("###", end="") for _ in range(len(nodes) * 2)]
    print()

    matrix = [[" + " for __ in range(len(nodes) * 2)] for _ in range(len(nodes) * 2)]
    for node in nodes:
        matrix[node.x][node.y] = f"N-{node.id}"
        if node.is_gw:
            matrix[node.x][node.y] = f'\033[92m{matrix[node.x][node.y]}\033[0m'

    for row in matrix:
        print("".join(row))
        print()

    [print("###", end="") for _ in range(len(nodes) * 2)]
    print()


def create_nodes(nodes: List[Node]) -> int:
    gw_id = randint(0, len(nodes) - 1)

    for i in range(len(nodes)):
        nodes[i].id = i

        randx = randint(0, len(nodes) * 2 - 1)
        randy = randint(0, len(nodes) * 2 - 1)
        nodes[i].x = randx
        nodes[i].y = randy

        nodes[i].is_gw = False

    nodes[gw_id].is_gw = True
    return gw_id


def get_connected_nodes(nodes: List[Node], gw_id: int, dislimit: int) -> List[id]:
    # create neighbors
    neighbors = dict()
    for node in nodes:
        for othernode in nodes:
            if node.id == othernode.id or get_distance(node, othernode) > dislimit:
                continue
            if node.id not in neighbors:
                neighbors[node.id] = []
            neighbors[node.id].append(othernode.id)

    pprint(neighbors)

    # bfs to find the connected nodes
    visited = set()
    queue = deque()
    queue.append(gw_id)

    while queue:
        cur_id = queue.popleft()

        cur_neighbors = neighbors.get(cur_id, [])

        if cur_id in visited:
            continue

        for neighbor in cur_neighbors:
            visited.add(neighbor)
            queue.append(neighbor)

    return list(visited)


def main():
    size = 10
    dislim = 10

    nodes = [Node() for _ in range(size)]
    gw_id = create_nodes(nodes)

    print("Gateway:", gw_id)
    print_nodes(nodes)

    connected_nodes = get_connected_nodes(nodes, gw_id, dislim)
    print("\nConnected Nodes:", connected_nodes)


if __name__ == "__main__":
    main()
