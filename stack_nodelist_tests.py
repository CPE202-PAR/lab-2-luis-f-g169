import unittest
from stack_nodelist import *
        
class TestLab2(unittest.TestCase):

    # WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.

    def test_is_empty(self) -> None:
        stack = Stack()
        self.assertTrue(stack.is_empty())

if __name__ == '__main__': 
    unittest.main()
