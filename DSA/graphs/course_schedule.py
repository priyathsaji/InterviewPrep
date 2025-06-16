"""
Problem Statement:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Input Format:
- numCourses: int - Total number of courses
- prerequisites: List[List[int]] - List of prerequisite pairs [course, prerequisite]

Output Format:
- bool - True if all courses can be finished, False otherwise

Example:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- All the pairs prerequisites[i] are unique.

Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
Space Complexity: O(V + E)
"""

from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Return true if all courses can be finished, false otherwise.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        numCourses = 2
        prerequisites = [[1,0]]
        self.assertTrue(self.solution.canFinish(numCourses, prerequisites))
    
    def test_example2(self):
        numCourses = 2
        prerequisites = [[1,0],[0,1]]
        self.assertFalse(self.solution.canFinish(numCourses, prerequisites))
    
    def test_no_prerequisites(self):
        numCourses = 3
        prerequisites = []
        self.assertTrue(self.solution.canFinish(numCourses, prerequisites))
    
    def test_single_course(self):
        numCourses = 1
        prerequisites = []
        self.assertTrue(self.solution.canFinish(numCourses, prerequisites))
    
    def test_linear_dependency(self):
        numCourses = 4
        prerequisites = [[1,0],[2,1],[3,2]]
        self.assertTrue(self.solution.canFinish(numCourses, prerequisites))
    
    def test_multiple_dependencies(self):
        numCourses = 4
        prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        self.assertTrue(self.solution.canFinish(numCourses, prerequisites))
    
    def test_cycle_in_middle(self):
        numCourses = 5
        prerequisites = [[1,0],[2,1],[1,2],[3,2],[4,3]]
        self.assertFalse(self.solution.canFinish(numCourses, prerequisites))
    
    def test_cycle_at_end(self):
        numCourses = 4
        prerequisites = [[1,0],[2,1],[3,2],[2,3]]
        self.assertFalse(self.solution.canFinish(numCourses, prerequisites))
    
    def test_cycle_at_start(self):
        numCourses = 4
        prerequisites = [[0,1],[1,0],[2,1],[3,2]]
        self.assertFalse(self.solution.canFinish(numCourses, prerequisites))
    
    def test_multiple_cycles(self):
        numCourses = 6
        prerequisites = [[1,0],[0,1],[2,1],[1,2],[3,2],[4,3],[5,4],[4,5]]
        self.assertFalse(self.solution.canFinish(numCourses, prerequisites))
    
    def test_disconnected_graph(self):
        numCourses = 4
        prerequisites = [[1,0],[3,2]]
        self.assertTrue(self.solution.canFinish(numCourses, prerequisites))
    
    def test_maximum_constraints(self):
        numCourses = 2000
        prerequisites = [[i,i+1] for i in range(1999)]
        self.assertTrue(self.solution.canFinish(numCourses, prerequisites))
    
    def test_maximum_prerequisites(self):
        numCourses = 100
        prerequisites = [[i,j] for i in range(1,100) for j in range(i)]
        self.assertTrue(self.solution.canFinish(numCourses, prerequisites))
    
    def test_self_loop(self):
        numCourses = 3
        prerequisites = [[0,0],[1,0],[2,1]]
        self.assertFalse(self.solution.canFinish(numCourses, prerequisites))
    
    def test_complex_dependency(self):
        numCourses = 6
        prerequisites = [[1,0],[2,0],[3,1],[4,2],[5,3],[5,4]]
        self.assertTrue(self.solution.canFinish(numCourses, prerequisites))

if __name__ == '__main__':
    unittest.main() 