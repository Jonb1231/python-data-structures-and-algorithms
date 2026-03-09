
from structures.dynamic_array import DynamicArray
from structures.graph import Graph, LatticeGraph
from structures.map import Map
from structures.pqueue import PriorityQueue


def _reset_visits(graph: Graph | LatticeGraph) -> None:
    for node in graph.get_all_nodes():
        node.visited = False


def bfs_traversal(graph: Graph | LatticeGraph, origin: int, goal: int) -> tuple[DynamicArray, DynamicArray]:
    visited_order = DynamicArray()
    path = DynamicArray()
    predecessors = Map()
    queue = PriorityQueue()
    _reset_visits(graph)
    queue.insert_fifo(origin)
    predecessors.insert_kv(origin, None)
    graph.get_node(origin).set_visited()

    while not queue.is_empty():
        current = queue.remove_min()
        visited_order.append(current)
        if current == goal:
            while current is not None:
                path.append(current)
                current = predecessors[current]
            path.reverse()
            return path, visited_order

        for neighbor in graph.get_neighbours(current):
            neighbor_id = neighbor.get_id()
            if not neighbor.get_visited():
                predecessors.insert_speedy(neighbor_id, current)
                neighbor.set_visited()
                queue.insert_fifo(neighbor_id)

    return path, visited_order


def dijkstra_traversal(graph: Graph, origin: int) -> DynamicArray:
    valid_locations = DynamicArray()
    queue = PriorityQueue()
    visited = Map()
    graph.set_nodes(origin)

    for vertex in graph.get_all_nodes():
        queue.insert(vertex.get_data(), vertex.get_id())

    while queue.get_size():
        current_distance = queue.get_min_priority()
        current_id = queue.remove_min()

        if visited.find(current_id) is not None:
            continue

        visited.insert_kv(current_id, current_distance)
        from structures.entry import Entry
        valid_locations.append(Entry(current_id, current_distance))

        for neighbor, weight in graph.get_neighbours(current_id):
            new_dist = current_distance + weight
            if new_dist < neighbor.get_data():
                neighbor._data = new_dist
                queue.insert(new_dist, neighbor.get_id())

    return valid_locations


def dfs_traversal(graph: Graph | LatticeGraph, origin: int, goal: int) -> tuple[DynamicArray, DynamicArray]:
    visited_order = DynamicArray()
    path = DynamicArray()
    predecessors = Map()
    _reset_visits(graph)

    stack = [origin]
    predecessors.insert_kv(origin, None)

    while stack:
        current = stack.pop()
        node = graph.get_node(current)
        if node.get_visited():
            continue
        node.set_visited()
        visited_order.append(current)

        if current == goal:
            while current is not None:
                path.append(current)
                current = predecessors[current]
            path.reverse()
            return path, visited_order

        neighbors = graph.get_neighbours(current)
        iterable = list(neighbors)
        iterable.reverse()
        for neighbor in iterable:
            neighbor_id = neighbor.get_id()
            if not graph.get_node(neighbor_id).get_visited() and predecessors.find(neighbor_id) is None:
                predecessors.insert_kv(neighbor_id, current)
                stack.append(neighbor_id)

    return path, visited_order
