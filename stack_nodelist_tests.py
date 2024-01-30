import unittest
from stack_nodelist import *
        
class TestLab2(unittest.TestCase):

    # WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.

    def test_is_empty(self) -> None:
        stack = Stack()
        self.assertTrue(stack.is_empty())

    def test_is_empty2(self) -> None:
        stack1 = Stack()
        stack1.push(6)
        self.assertFalse(stack1.is_empty())

    def test_pop(self) -> None:
        stack2 = Stack()
        with self.assertRaises(IndexError):
            stack2.pop()
    
    def test_pop2(self) -> None:
        stack3 = Stack()
        stack3.push(3)
        stack3.push(4)
        self.assertEqual(stack3.pop(), 4)
    
    def test_peek(self) -> None:
        stack4 = Stack()
        with self.assertRaises(IndexError):
            stack4.peek()
    
    def test_peek2(self) -> None:
        stack5 = Stack()
        stack5.push(5)
        self.assertEqual(stack5.peek(), 5)
    
    def test_size(self) -> None:
        stack6 = Stack()
        stack6.push(6)
        stack6.push(5)
        stack6.push(10)
        self.assertEqual(stack6.size(), 3)

if __name__ == '__main__': 
    unittest.main()
