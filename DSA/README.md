# Data Structures and Algorithms

This directory contains implementations of various data structures and algorithms, organized by category.

## Structure

Each implementation is organized in its own Python file with the following structure:
- Algorithm/Data Structure description
- Time and Space complexity analysis
- Implementation details
- Unit tests
- Example usage

## Available Problems

### Algorithms

#### Greedy Algorithms
- Stoer-Wagner Algorithm for Minimum Cut
  - Basic minimum cut computation
  - Minimum cut with required edges
  - Minimum cut with vertex capacity constraints
  - Maximum flow computation

#### Divide and Conquer
- Merge Sort
  - Basic merge sort
  - In-place merge sort
  - Custom key function support
- Quick Sort
  - Basic quick sort
  - In-place quick sort
  - Quick select
  - Custom key function support
- Binary Search
  - Iterative binary search
  - Recursive binary search
  - First/last occurrence
  - Closest element
- Karatsuba Algorithm
  - Basic integer multiplication
  - Polynomial multiplication
  - Matrix multiplication
  - String-based multiplication
- Closest Pair of Points
  - 2D closest pair
  - 3D closest pair
  - k closest pairs
  - Manhattan distance closest pair
- Fast Fourier Transform (FFT)
  - Basic FFT
  - Inverse FFT
  - 2D FFT
  - Polynomial multiplication using FFT
  - Real-valued FFT
- Convex Hull
  - 2D convex hull
  - 3D convex hull
  - k-hull
  - Area and perimeter calculation
- Skyline Problem
  - Basic skyline computation
  - 3D skyline
  - Area and perimeter calculation
  - Maximum height calculation

#### Dynamic Programming
- Longest Common Subsequence (LCS)
  - Basic LCS computation
  - LCS length calculation
  - Finding all LCS
  - LCS with constraints
  - LCS with weighted characters
- Knapsack Problem
  - 0-1 Knapsack
  - Fractional Knapsack
  - Unbounded Knapsack
  - Multiple Knapsacks
  - Knapsack with constraints
- Matrix Chain Multiplication
  - Basic matrix chain multiplication
  - Custom cost function
  - Additional constraints
  - Parallel processing
  - Memory constraints
- Fibonacci
  - Basic Fibonacci computation
  - Memoized Fibonacci
  - Iterative Fibonacci
  - Matrix exponentiation
  - Fibonacci with modulo

### Data Structures

#### Trees
- Binary Search Tree
  - Basic BST operations
  - Balanced BST
  - Custom key function support
  - Range queries
  - Order statistics
- AVL Tree
  - Basic AVL operations
  - Custom key function support
  - Range queries
  - Order statistics
- Red-Black Tree
  - Basic RBT operations
  - Custom key function support
  - Range queries
  - Order statistics
- B-Tree
  - Basic B-tree operations
  - Custom key function support
  - Range queries
  - Order statistics
- Trie
  - Basic trie operations
  - Prefix search
  - Pattern matching
  - Word suggestions

#### Graphs
- Graph
  - Basic graph operations
  - Custom vertex/edge types
  - Path finding
  - Cycle detection
- Directed Graph
  - Basic directed graph operations
  - Custom vertex/edge types
  - Path finding
  - Cycle detection
- Weighted Graph
  - Basic weighted graph operations
  - Custom vertex/edge types
  - Path finding
  - Cycle detection
- Directed Weighted Graph
  - Basic directed weighted graph operations
  - Custom vertex/edge types
  - Path finding
  - Cycle detection

## How to Use

1. Navigate to the specific algorithm or data structure directory
2. Read the implementation details and complexity analysis
3. Run the tests to verify the implementation
4. Use the implementation in your own code

## Running Tests

To run tests for a specific implementation:
```bash
python implementation_name.py
```

To run all tests in a directory:
```bash
python -m unittest discover
```

## Best Practices

1. Always document your approach before implementing
2. Include edge cases in your test cases
3. Analyze time and space complexity
4. Consider multiple approaches if possible
5. Add comments explaining complex logic 