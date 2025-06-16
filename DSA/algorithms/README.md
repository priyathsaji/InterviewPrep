# Algorithms Implementation

This directory contains implementations of fundamental algorithms in Python. Each algorithm is implemented as a separate module with its own test cases and complexity analysis.

## Categories

### 1. Sorting Algorithms
- **Comparison-based Sorts**
  - Bubble Sort (`sorting/bubble_sort.py`)
  - Selection Sort (`sorting/selection_sort.py`)
  - Insertion Sort (`sorting/insertion_sort.py`)
  - Merge Sort (`sorting/merge_sort.py`)
  - Quick Sort (`sorting/quick_sort.py`)
  - Heap Sort (`sorting/heap_sort.py`)
- **Non-comparison Sorts**
  - Counting Sort (`sorting/counting_sort.py`)
  - Radix Sort (`sorting/radix_sort.py`)
  - Bucket Sort (`sorting/bucket_sort.py`)

### 2. Graph Algorithms
- **Traversal**
  - Breadth-First Search (BFS) (`graph/bfs.py`)
  - Depth-First Search (DFS) (`graph/dfs.py`)
- **Shortest Path**
  - Dijkstra's Algorithm (`graph/dijkstra.py`)
  - Bellman-Ford Algorithm (`graph/bellman_ford.py`)
  - Floyd-Warshall Algorithm (`graph/floyd_warshall.py`)
- **Minimum Spanning Tree**
  - Kruskal's Algorithm (`graph/kruskal.py`)
  - Prim's Algorithm (`graph/prim.py`)
- **Topological Sort** (`graph/topological_sort.py`)

### 3. Dynamic Programming
- **Classic Problems**
  - Fibonacci (`dp/fibonacci.py`)
  - Longest Common Subsequence (`dp/lcs.py`)
  - Longest Increasing Subsequence (`dp/lis.py`)
  - Matrix Chain Multiplication (`dp/matrix_chain.py`)
  - 0/1 Knapsack (`dp/knapsack.py`)
  - Coin Change (`dp/coin_change.py`)

### 4. String Algorithms
- **Pattern Matching**
  - Naive String Matching (`string/naive_matching.py`)
  - Rabin-Karp Algorithm (`string/rabin_karp.py`)
  - KMP Algorithm (`string/kmp.py`)
- **String Manipulation**
  - Longest Palindromic Substring (`string/longest_palindrome.py`)
  - String Permutations (`string/permutations.py`)
  - String Compression (`string/compression.py`)

### 5. Search Algorithms
- **Array Search**
  - Binary Search (`search/binary_search.py`)
  - Linear Search (`search/linear_search.py`)
  - Jump Search (`search/jump_search.py`)
  - Interpolation Search (`search/interpolation_search.py`)
- **Tree Search**
  - Binary Tree Traversal (`search/tree_traversal.py`)
  - Binary Search Tree Operations (`search/bst_operations.py`)

### 6. Greedy Algorithms
- **Scheduling**
  - Activity Selection (`greedy/activity_selection.py`)
  - Job Scheduling (`greedy/job_scheduling.py`)
- **Optimization**
  - Huffman Coding (`greedy/huffman.py`)
  - Fractional Knapsack (`greedy/fractional_knapsack.py`)

### 7. Divide and Conquer
- **Array Problems**
  - Maximum Subarray (`divide_conquer/max_subarray.py`)
  - Closest Pair of Points (`divide_conquer/closest_pair.py`)
- **Matrix Operations**
  - Strassen's Matrix Multiplication (`divide_conquer/strassen.py`)

## Usage

Each algorithm implementation includes:
- A function or class implementation
- Comprehensive test cases
- Time and space complexity analysis
- Example usage
- Edge cases handling

## Testing

Run tests for each implementation using:
```bash
python -m unittest <filename>_test.py
```

## Complexity Analysis

Each implementation includes detailed time and space complexity analysis in its documentation.

## Additional Algorithms to Consider

1. **Advanced Graph Algorithms**
   - Maximum Flow (Ford-Fulkerson)
   - Strongly Connected Components
   - Articulation Points and Bridges

2. **Advanced Dynamic Programming**
   - Edit Distance
   - Optimal Binary Search Tree
   - Longest Palindromic Subsequence

3. **Advanced String Algorithms**
   - Suffix Array
   - Suffix Automaton
   - Aho-Corasick Algorithm

4. **Advanced Search Algorithms**
   - A* Search
   - IDA* Search
   - Beam Search

5. **Advanced Optimization**
   - Simulated Annealing
   - Genetic Algorithms
   - Branch and Bound 