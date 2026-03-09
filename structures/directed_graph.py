
from structures.map import Map


class DirectedGraph:
    """Small adjacency-list directed graph wrapper backed by Map."""

    def __init__(self):
        self.graph = Map()

    def get_size(self):
        return self.graph.get_size()

    def get_node(self, node_id):
        return self.graph.find(node_id)

    def get_keys(self):
        return self.graph.get_keys()

    def add_node(self, node):
        if self.graph.find(node) is None:
            self.graph[node] = []

    def add_edge(self, start_node, end_node):
        neighbors = self.graph.find(start_node)
        if neighbors is None:
            self.graph[start_node] = [end_node]
        else:
            neighbors.append(end_node)

    def display(self):
        for key in self.graph.get_keys():
            print(f"{key} -> {self.graph.find(key)}")

    def get_neighbors(self, node):
        return self.graph.find(node)
