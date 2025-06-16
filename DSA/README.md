# Blind 75 Problems

This directory contains solutions to the Blind 75 problems, a curated list of the most important coding interview questions.

## Structure

Each problem is organized in its own Python file with the following structure:
- Problem statement
- Input/Output format
- Example test cases
- Solution implementation
- Unit tests
- Time and Space complexity analysis

## How to Use

1. Copy the `template.py` file and rename it according to the problem (e.g., `two_sum.py`)
2. Fill in the problem statement, input/output format, and constraints
3. Implement your solution in the `solve_problem` method
4. Add test cases in the `TestSolution` class
5. Run the file to test your solution: `python problem_name.py`

## Problem Categories

The problems are organized into the following categories:
1. Arrays & Strings
2. Linked Lists
3. Trees & Graphs
4. Dynamic Programming
5. Design
6. Math & Logic

## Best Practices

1. Always document your approach before implementing
2. Include edge cases in your test cases
3. Analyze time and space complexity
4. Consider multiple approaches if possible
5. Add comments explaining complex logic

## Running Tests

To run tests for a specific problem:
```bash
python problem_name.py
```

To run all tests in the directory:
```bash
python -m unittest discover
``` 