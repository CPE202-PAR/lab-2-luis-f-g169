import unittest
from stack_array import Stack
        
class TestLab2(unittest.TestCase):

# WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.

    def test_is_empty(self) -> None:
        stack = Stack(5)
        self.assertTrue(stack.is_empty())

if __name__ == '__main__': 
    unittest.main()
