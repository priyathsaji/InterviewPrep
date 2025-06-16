# Data Structures Implementation

This directory contains implementations of fundamental data structures in Python. Each data structure is implemented as a separate module with its own test cases.

## Implemented Data Structures

1. **Stack**
   - LIFO (Last In First Out) data structure
   - Basic operations: push, pop, peek, is_empty
   - Implementation: `stack.py`

2. **Queue**
   - FIFO (First In First Out) data structure
   - Basic operations: enqueue, dequeue, peek, is_empty
   - Implementation: `queue.py`

3. **Priority Queue**
   - Queue where elements have priority
   - Basic operations: insert, extract_max/min, peek
   - Implementation: `priority_queue.py`

4. **Heap**
   - Binary Heap implementation
   - Both Min and Max heap variants
   - Basic operations: insert, extract_max/min, heapify
   - Implementation: `heap.py`

5. **Linked List**
   - Singly and Doubly linked list implementations
   - Basic operations: insert, delete, search
   - Implementation: `linked_list.py`

6. **Binary Search Tree**
   - Self-balancing BST implementation
   - Basic operations: insert, delete, search
   - Implementation: `binary_search_tree.py`

7. **Trie (Prefix Tree)**
   - Tree-like data structure for storing strings
   - Basic operations: insert, search, delete, prefix search
   - Implementation: `trie.py`

8. **Hash Table**
   - Key-value pair storage with O(1) average case operations
   - Basic operations: put, get, remove, contains_key
   - Implementation: `hash_table.py`

9. **Graph**
   - Both directed and undirected graph implementations
   - Basic operations: add/remove vertex/edge, get neighbors
   - Implementation: `graph.py`

## Usage

Each data structure implementation includes:
- A class implementation with all basic operations
- Comprehensive test cases
- Time and space complexity analysis
- Example usage

## Testing

Run tests for each implementation using:
```bash
python -m unittest <filename>_test.py
```

## Complexity Analysis

Each implementation includes detailed time and space complexity analysis for all operations in its documentation.

## Additional Data Structures to Consider

1. **Advanced Tree Structures**
   - AVL Tree
   - Red-Black Tree
   - B-Tree
   - Segment Tree
   - Fenwick Tree (Binary Indexed Tree)

2. **Advanced Graph Structures**
   - Weighted Graph
   - Disjoint Set (Union-Find)
   - Minimum Spanning Tree
   - Shortest Path Algorithms

3. **Specialized Data Structures**
   - Skip List
   - Bloom Filter
   - LRU Cache
   - Circular Buffer
   - Suffix Tree/Array 