"""
Problem Statement:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Input Format:
- numCourses: int - Total number of courses
- prerequisites: List[List[int]] - List of prerequisite pairs [course, prerequisite]

Output Format:
- List[int] - Ordering of courses to take, or empty array if impossible

Example:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3]
Explanation: One valid course order is [0,1,2,3]. Another valid course order is [0,2,1,3].

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: []
Explanation: It is impossible to finish all courses.

Constraints:
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- ai != bi
- All the pairs prerequisites[i] are unique.

Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
Space Complexity: O(V + E)
"""

from typing import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Return the ordering of courses to take.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        numCourses = 4
        prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        result = self.solution.findOrder(numCourses, prerequisites)
        self.assertTrue(self._is_valid_order(result, numCourses, prerequisites))
    
    def test_example2(self):
        numCourses = 2
        prerequisites = [[1,0],[0,1]]
        self.assertEqual(self.solution.findOrder(numCourses, prerequisites), [])
    
    def test_no_prerequisites(self):
        numCourses = 3
        prerequisites = []
        result = self.solution.findOrder(numCourses, prerequisites)
        self.assertTrue(self._is_valid_order(result, numCourses, prerequisites))
    
    def test_single_course(self):
        numCourses = 1
        prerequisites = []
        result = self.solution.findOrder(numCourses, prerequisites)
        self.assertTrue(self._is_valid_order(result, numCourses, prerequisites))
    
    def test_linear_dependency(self):
        numCourses = 4
        prerequisites = [[1,0],[2,1],[3,2]]
        result = self.solution.findOrder(numCourses, prerequisites)
        self.assertTrue(self._is_valid_order(result, numCourses, prerequisites))
    
    def test_multiple_dependencies(self):
        numCourses = 4
        prerequisites = [[1,0],[2,0],[3,0]]
        result = self.solution.findOrder(numCourses, prerequisites)
        self.assertTrue(self._is_valid_order(result, numCourses, prerequisites))
    
    def test_cycle_in_middle(self):
        numCourses = 5
        prerequisites = [[1,0],[2,1],[1,2],[3,2],[4,3]]
        self.assertEqual(self.solution.findOrder(numCourses, prerequisites), [])
    
    def test_cycle_at_end(self):
        numCourses = 4
        prerequisites = [[1,0],[2,1],[3,2],[2,3]]
        self.assertEqual(self.solution.findOrder(numCourses, prerequisites), [])
    
    def test_cycle_at_start(self):
        numCourses = 4
        prerequisites = [[0,1],[1,0],[2,1],[3,2]]
        self.assertEqual(self.solution.findOrder(numCourses, prerequisites), [])
    
    def test_multiple_cycles(self):
        numCourses = 6
        prerequisites = [[1,0],[0,1],[2,1],[1,2],[3,2],[4,3],[5,4],[4,5]]
        self.assertEqual(self.solution.findOrder(numCourses, prerequisites), [])
    
    def test_disconnected_graph(self):
        numCourses = 4
        prerequisites = [[1,0],[3,2]]
        result = self.solution.findOrder(numCourses, prerequisites)
        self.assertTrue(self._is_valid_order(result, numCourses, prerequisites))
    
    def test_maximum_constraints(self):
        numCourses = 2000
        prerequisites = [[i,i+1] for i in range(1999)]
        result = self.solution.findOrder(numCourses, prerequisites)
        self.assertTrue(self._is_valid_order(result, numCourses, prerequisites))
    
    def test_maximum_prerequisites(self):
        numCourses = 100
        prerequisites = [[i,j] for i in range(1,100) for j in range(i)]
        result = self.solution.findOrder(numCourses, prerequisites)
        self.assertTrue(self._is_valid_order(result, numCourses, prerequisites))
    
    def test_self_loop(self):
        numCourses = 3
        prerequisites = [[0,0],[1,0],[2,1]]
        self.assertEqual(self.solution.findOrder(numCourses, prerequisites), [])
    
    def test_complex_dependency(self):
        numCourses = 6
        prerequisites = [[1,0],[2,0],[3,1],[4,2],[5,3],[5,4]]
        result = self.solution.findOrder(numCourses, prerequisites)
        self.assertTrue(self._is_valid_order(result, numCourses, prerequisites))
    
    def _is_valid_order(self, order: List[int], numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Helper method to validate if the course order is valid.
        """
        if not order:
            return False
        
        # Check if all courses are included
        if len(order) != numCourses or len(set(order)) != numCourses:
            return False
        
        # Check if prerequisites are satisfied
        course_to_index = {course: index for index, course in enumerate(order)}
        for course, prereq in prerequisites:
            if course_to_index[prereq] > course_to_index[course]:
                return False
        
        return True

if __name__ == '__main__':
    unittest.main() 