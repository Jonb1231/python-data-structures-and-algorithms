
from structures.bit_vector import BitVector
from structures.bloom_filter import BloomFilter
from structures.entry import Entry
from structures.graph import Graph, LatticeGraph
from structures.map import Map
from structures.pqueue import PriorityQueue


def maybe_maybe_maybe(database: list[str], query: list[str]) -> list[str]:
    """Return query k-mers that are likely present using a Bloom filter."""
    result = []
    bloom = BloomFilter(max(1, len(database)))
    for kmer in database:
        bloom.insert(kmer)
    for kmer in query:
        if bloom.contains(kmer):
            result.append(kmer)
    return result


def chin_bicken(graph: Graph | LatticeGraph, origin: int) -> list[tuple[str, int]]:
    """Count labels reachable from an origin using graph traversal."""
    visited = BitVector()
    visited.allocate(max(1, len(graph.get_all_nodes()) * 3))
    label_counts = Map()
    queue = PriorityQueue()
    queue.insert_fifo(origin)
    visited.set_at(origin)

    while not queue.is_empty():
        current = queue.remove_min()
        current_node = graph.get_node(current)
        label = current_node.get_data()
        if label_counts.find(label) is not None:
            label_counts.incr_value(label)
        else:
            label_counts.insert_kv(label, 1)

        for neighbor in graph.get_neighbours(current):
            neighbor_id = neighbor.get_id()
            if visited.get_at(neighbor_id) == 0:
                visited.set_at(neighbor_id)
                queue.insert_fifo(neighbor_id)

    return [(key, label_counts.find(key)) for key in label_counts.get_keys()]
