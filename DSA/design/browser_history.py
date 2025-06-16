"""
Problem Statement:
Design a browser history system that supports forward and backward navigation.

Implement the BrowserHistory class:
- BrowserHistory(string homepage) initializes the object with the homepage of the browser.
- void visit(string url) visits url from the current page. It clears up all the forward history.
- string back(int steps) moves steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
- string forward(int steps) moves steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after moving forward in history at most steps.

Input Format:
- homepage: str - The initial URL
- url: str - The URL to visit
- steps: int - Number of steps to move back/forward

Output Format:
- str - The current URL after navigation

Example:
Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output: [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Constraints:
- 1 <= homepage.length <= 20
- 1 <= url.length <= 20
- 1 <= steps <= 100
- homepage and url consist of  '.' or lower case English letters.
- At most 5000 calls will be made to visit, back, and forward.

Time Complexity: O(1) for all operations
Space Complexity: O(n) where n is the number of URLs in history
"""

class BrowserHistory:
    def __init__(self, homepage: str):
        """
        Initialize your data structure here.
        We use a list to store the history and an index to track the current position.
        """
    
    def visit(self, url: str) -> None:
        """
        Visits url from the current page. It clears up all the forward history.
        """
        raise NotImplementedError("Solution not implemented")
    def back(self, steps: int) -> str:
        """
        Move steps back in history.
        """
        raise NotImplementedError("Solution not implemented")
    
    def forward(self, steps: int) -> str:
        """
        Move steps forward in history.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestBrowserHistory(unittest.TestCase):
    def test_example1(self):
        browser = BrowserHistory("leetcode.com")
        browser.visit("google.com")
        browser.visit("facebook.com")
        browser.visit("youtube.com")
        self.assertEqual(browser.back(1), "facebook.com")
        self.assertEqual(browser.back(1), "google.com")
        self.assertEqual(browser.forward(1), "facebook.com")
        browser.visit("linkedin.com")
        self.assertEqual(browser.forward(2), "linkedin.com")
        self.assertEqual(browser.back(2), "google.com")
        self.assertEqual(browser.back(7), "leetcode.com")
    
    def test_example2(self):
        browser = BrowserHistory("homepage.com")
        browser.visit("page1.com")
        browser.visit("page2.com")
        self.assertEqual(browser.back(1), "page1.com")
        self.assertEqual(browser.forward(1), "page2.com")
        browser.visit("page3.com")
        self.assertEqual(browser.back(2), "homepage.com")
        self.assertEqual(browser.forward(1), "page1.com")
    
    def test_single_page(self):
        browser = BrowserHistory("homepage.com")
        self.assertEqual(browser.back(1), "homepage.com")
        self.assertEqual(browser.forward(1), "homepage.com")
    
    def test_multiple_visits(self):
        browser = BrowserHistory("start.com")
        urls = ["page1.com", "page2.com", "page3.com", "page4.com"]
        for url in urls:
            browser.visit(url)
        self.assertEqual(browser.back(2), "page2.com")
        browser.visit("newpage.com")
        self.assertEqual(browser.forward(1), "newpage.com")
        self.assertEqual(browser.back(3), "start.com")

if __name__ == '__main__':
    unittest.main() 