"""
Problem Statement:
Given a m * n matrix seats that represent seats distributions in a classroom. If a seat is broken, it is denoted by '#' character otherwise it is denoted by a '.' character.

Students can see the answers of those sitting next to the left, right, upper left and upper right, but cannot see the answers of students sitting directly in front or behind them.

Return the maximum number of students that can take the exam together without any cheating being possible.

Input Format:
- seats: List[List[str]] - Matrix representing the classroom seats

Output Format:
- int - Maximum number of students that can take the exam

Example:
Input: seats = [
    ["#",".","#","#",".","#"],
    [".","#","#","#","#","."],
    ["#",".","#","#",".","#"]
]
Output: 4
Explanation: Teacher can place 4 students in available seats so they don't cheat on the exam.

Input: seats = [
    [".","#"],
    ["#","#"],
    ["#","."],
    ["#","#"],
    [".","#"]
]
Output: 3
Explanation: Place all students in available seats.

Constraints:
- seats contains only characters '.' and '#'.
- m == len(seats)
- n == len(seats[i])
- 1 <= m <= 8
- 1 <= n <= 8

Time Complexity: O(m * 2^n) where m is the number of rows and n is the number of columns
Space Complexity: O(m * 2^n) where m is the number of rows and n is the number of columns
"""

class Solution:
    def maxStudents(self, seats: list[list[str]]) -> int:
        """
        Find the maximum number of students that can take the exam without cheating.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        seats = [
            ["#",".","#","#",".","#"],
            [".","#","#","#","#","."],
            ["#",".","#","#",".","#"]
        ]
        self.assertEqual(self.solution.maxStudents(seats), 4)
    
    def test_example2(self):
        seats = [
            [".","#"],
            ["#","#"],
            ["#","."],
            ["#","#"],
            [".","#"]
        ]
        self.assertEqual(self.solution.maxStudents(seats), 3)
    
    def test_single_seat(self):
        seats = [["."]]
        self.assertEqual(self.solution.maxStudents(seats), 1)
    
    def test_single_broken_seat(self):
        seats = [["#"]]
        self.assertEqual(self.solution.maxStudents(seats), 0)
    
    def test_two_seats_available(self):
        seats = [[".","."]]
        self.assertEqual(self.solution.maxStudents(seats), 1)
    
    def test_two_seats_broken(self):
        seats = [["#","#"]]
        self.assertEqual(self.solution.maxStudents(seats), 0)
    
    def test_three_seats_available(self):
        seats = [[".",".","."]]
        self.assertEqual(self.solution.maxStudents(seats), 2)
    
    def test_three_seats_alternating(self):
        seats = [[".","#","."]]
        self.assertEqual(self.solution.maxStudents(seats), 1)
    
    def test_two_rows_available(self):
        seats = [
            [".",".","."],
            [".",".","."]
        ]
        self.assertEqual(self.solution.maxStudents(seats), 4)
    
    def test_two_rows_alternating(self):
        seats = [
            [".","#","."],
            ["#",".","#"]
        ]
        self.assertEqual(self.solution.maxStudents(seats), 2)
    
    def test_all_broken(self):
        seats = [
            ["#","#","#"],
            ["#","#","#"],
            ["#","#","#"]
        ]
        self.assertEqual(self.solution.maxStudents(seats), 0)
    
    def test_all_available(self):
        seats = [
            [".",".","."],
            [".",".","."],
            [".",".","."]
        ]
        self.assertEqual(self.solution.maxStudents(seats), 4)
    
    def test_checkerboard(self):
        seats = [
            [".","#",".","#"],
            ["#",".","#","."],
            [".","#",".","#"]
        ]
        self.assertEqual(self.solution.maxStudents(seats), 6)

if __name__ == '__main__':
    unittest.main() 