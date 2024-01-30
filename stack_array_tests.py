import unittest
from stack_array import Stack
        
class TestLab2(unittest.TestCase):

# WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.

    def test_is_empty(self) -> None:
        stack = Stack(5)
        self.assertTrue(stack.is_empty())

    def test_is_empty2(self) -> None:
        stack2 = Stack(4)
        stack2.push(5)
        self.assertFalse(stack2.is_empty())
    
    def test_is_full(self) -> None:
        stack3 = Stack(1)
        stack3.push(5)
        self.assertTrue(stack3.is_full())

    def test_is_full2(self) -> None:
        stack4 = Stack(1)
        self.assertFalse(stack4.is_full())
    
    def test_push(self) -> None:
        stack5 = Stack(5)
        stack5.push(5)
        self.assertEqual(stack5.items[stack5.num_items-1], 5)

    def test_push2(self) -> None:
        stack6 = Stack(1)
        stack6.push(1)
        with self.assertRaises(IndexError):
            stack6.push(3)

    def test_pop(self):
        stack7 = Stack(2)
        with self.assertRaises(IndexError):
            stack7.pop()

    def test_pop2(self):
        stack8 = Stack(2)
        stack8.push(2)
        self.assertEqual(stack8.pop(), 2)

    def test_peek(self):
        stack9 = Stack(1)
        with self.assertRaises(IndexError):
            stack9.peek()

    def test_peek2(self):
        stack10 = Stack(2)
        stack10.push(1)
        self.assertEqual(stack10.peek(), 1)

    def test_size(self):
        stack11 = Stack(4)
        stack11.push(2)
        stack11.push(2)
        self.assertEqual(stack11.size(), 2)

if __name__ == '__main__': 
    unittest.main()
