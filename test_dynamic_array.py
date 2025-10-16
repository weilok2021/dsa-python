import unittest
from dynamic_array import DynamicArray  # replace with your actual file name

class TestDynamicArray(unittest.TestCase):

    def setUp(self):
        self.arr = DynamicArray()

    def test_initial_state(self):
        self.assertEqual(self.arr.size(), 0)
        self.assertGreaterEqual(self.arr.capacity(), 16)
        self.assertTrue(self.arr.is_empty())

    def test_push_and_at(self):
        for i in range(5):
            self.arr.push(i)
        self.assertEqual(self.arr.size(), 5)
        self.assertFalse(self.arr.is_empty())
        for i in range(5):
            self.assertEqual(self.arr.at(i), i)

    def test_push_triggers_resize(self):
        initial_capacity = self.arr.capacity()
        for i in range(initial_capacity + 1):
            self.arr.push(i)
        self.assertGreater(self.arr.capacity(), initial_capacity)

    def test_pop(self):
        for i in range(5):
            self.arr.push(i)
        last = self.arr.pop()
        self.assertEqual(last, 4)
        self.assertEqual(self.arr.size(), 4)


    def test_at_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.arr.at(0)
        self.arr.push(1)
        with self.assertRaises(IndexError):
            self.arr.at(2)

    def test_is_empty_behavior(self):
        self.assertTrue(self.arr.is_empty())
        self.arr.push(10)
        self.assertFalse(self.arr.is_empty())
        self.arr.pop()
        self.assertTrue(self.arr.is_empty())

if __name__ == '__main__':
    unittest.main()
