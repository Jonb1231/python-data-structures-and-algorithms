
from algorithms.pathfinding import bfs_traversal, dijkstra_traversal
from applications.warmup_challenges import k_cool, missing_odds
from structures.graph import Graph, Node
from structures.map import Map
from structures.pqueue import PriorityQueue


def main() -> None:
    pq = PriorityQueue()
    for priority, label in [(5, 'low'), (1, 'urgent'), (3, 'normal')]:
        pq.insert(priority, label)
    print('PriorityQueue min:', pq.get_min_value())

    phonebook = Map()
    phonebook['alice'] = 1111
    phonebook['bob'] = 2222
    print('Map lookup:', phonebook['alice'])

    nodes = [Node(0), Node(1), Node(2), Node(3)]
    edges = [[(1, 1), (2, 4)], [(2, 2), (3, 5)], [(3, 1)], []]
    graph = Graph(nodes=nodes, edges=edges, weighted=True)
    print('Shortest paths from 0:', [(e.get_key(), e.get_value()) for e in dijkstra_traversal(graph, 0)])

    graph2 = Graph(nodes=[Node(i) for i in range(4)], edges=[[1, 2], [3], [3], []], weighted=False)
    path, visited = bfs_traversal(graph2, 0, 3)
    print('BFS path:', path.to_list())
    print('Visited order:', visited.to_list())

    print('k_cool(10, 42):', k_cool(10, 42))
    print('missing_odds([4,1,8,5]):', missing_odds([4, 1, 8, 5]))


if __name__ == '__main__':
    main()
