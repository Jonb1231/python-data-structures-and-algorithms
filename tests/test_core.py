
import unittest

from algorithms.pathfinding import bfs_traversal, dfs_traversal, dijkstra_traversal
from applications.warmup_challenges import k_cool, missing_odds, number_game, road_illumination
from structures.bit_vector import BitVector
from structures.bloom_filter import BloomFilter
from structures.dynamic_array import DynamicArray
from structures.graph import Graph, Node
from structures.map import Map
from structures.pqueue import PriorityQueue


class CoreTests(unittest.TestCase):
    def test_dynamic_array(self):
        arr = DynamicArray()
        for value in [3, 1, 2]:
            arr.append(value)
        arr.sort()
        self.assertEqual(arr.to_list(), [1, 2, 3])
        arr.reverse()
        self.assertEqual(arr.to_list(), [3, 2, 1])

    def test_bit_vector(self):
        bv = BitVector()
        bv.allocate(10)
        bv.set_at(3)
        self.assertEqual(bv.get_at(3), 1)
        bv.unset_at(3)
        self.assertEqual(bv.get_at(3), 0)

    def test_map(self):
        m = Map()
        m.insert_kv('a', 1)
        m.insert_kv('b', 2)
        self.assertEqual(m.find('a'), 1)
        m.remove('a')
        self.assertIsNone(m.find('a'))

    def test_priority_queue(self):
        pq = PriorityQueue()
        pq.insert(5, 'low')
        pq.insert(1, 'high')
        pq.insert(3, 'mid')
        self.assertEqual(pq.remove_min(), 'high')
        self.assertEqual(pq.remove_min(), 'mid')
        self.assertEqual(pq.remove_min(), 'low')

    def test_bloom_filter(self):
        bloom = BloomFilter(10)
        bloom.insert('hello')
        self.assertTrue(bloom.contains('hello'))

    def test_graph_algorithms(self):
        weighted = Graph(nodes=[Node(i) for i in range(4)], edges=[[(1, 1), (2, 4)], [(2, 2), (3, 6)], [(3, 1)], []], weighted=True)
        distances = [(entry.get_key(), entry.get_value()) for entry in dijkstra_traversal(weighted, 0)]
        self.assertEqual(distances[0], (0, 0))
        self.assertIn((3, 4), distances)

        unweighted = Graph(nodes=[Node(i) for i in range(4)], edges=[[1, 2], [3], [3], []], weighted=False)
        path, visited = bfs_traversal(unweighted, 0, 3)
        self.assertEqual(path.to_list(), [0, 1, 3])
        self.assertEqual(visited.to_list()[0], 0)
        path2, _ = dfs_traversal(unweighted, 0, 3)
        self.assertEqual(path2.to_list()[0], 0)
        self.assertEqual(path2.to_list()[-1], 3)

    def test_warmup_applications(self):
        self.assertEqual(missing_odds([4, 1, 8, 5]), 10)
        self.assertEqual(k_cool(10, 42), 101010)
        self.assertEqual(number_game([5, 2, 7, 3]), ('Bob', 5))
        self.assertAlmostEqual(road_illumination(15, [15, 5, 3, 7, 9, 14, 0]), 2.5)


if __name__ == '__main__':
    unittest.main()
