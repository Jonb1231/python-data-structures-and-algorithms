
# Python Data Structures and Algorithms

A curated Python project implementing data structures and algorithms from scratch, including dynamic arrays, bit vectors, linked lists, hash maps, priority queues, bloom filters, and graph traversal/pathfinding routines.

This repository was built by combining the strongest parts of two university projects and then cleaning, restructuring, and documenting them for portfolio use.

## What this project demonstrates

- custom core data structures implemented without relying on Python's built-in equivalents
- algorithmic problem solving using those structures in realistic tasks
- graph traversal and shortest-path search
- probabilistic membership testing with a Bloom filter
- clean modular organisation across `structures`, `algorithms`, and `applications`

## Included modules

### `structures/`
- `dynamic_array.py` — resizable array with sorting support
- `bit_vector.py` — compact bit storage
- `linked_list.py` — doubly linked list
- `map.py` — hash map with separate chaining
- `pqueue.py` — binary min-heap priority queue
- `bloom_filter.py` — probabilistic set membership
- `graph.py` and `directed_graph.py` — graph representations used by traversal algorithms

### `algorithms/`
- `pathfinding.py` — BFS, DFS, and Dijkstra traversal
- `problems.py` — examples using the project data structures in traversal and filtering tasks

### `applications/`
- `warmup_challenges.py` — selected algorithmic challenge functions adapted into a cleaner module:
  - `missing_odds`
  - `k_cool`
  - `number_game`
  - `road_illumination`

## Example usage

```bash
python examples.py
```

## Running tests

```bash
python -m unittest discover -s tests
```

## Why this repo is on my GitHub

I wanted one repository that highlights CS fundamentals clearly for graduate software roles: building core data structures, applying them to algorithmic problems, and organising the code like a real project rather than leaving it as raw coursework.
