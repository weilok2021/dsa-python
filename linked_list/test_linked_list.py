import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    
    def setUp(self):
        self.ll = LinkedList()

    # --- empty() and size() tests ---
    def test_empty_list_initially(self):
        self.assertTrue(self.ll.is_empty(), "List should be empty initially")
        self.assertEqual(self.ll.size(), 0, "Initial size should be 0")

    # --- push_front() and front() tests ---
    def test_push_front_single_element(self):
        self.ll.push_front(10)
        self.assertFalse(self.ll.is_empty(), "List should not be empty after push_front")
        self.assertEqual(self.ll.size(), 1, "Size should be 1 after adding one element")
        self.assertEqual(self.ll.front(), 10, "Front should return the first inserted value")

    def test_push_front_multiple_elements(self):
        for val in [10, 20, 30]:
            self.ll.push_front(val)
        self.assertEqual(self.ll.size(), 3)
        # Since push_front inserts at the head, last inserted should be at front
        self.assertEqual(self.ll.front(), 30, "Front should be the last pushed value")

    # --- value_at(index) tests ---
    def test_value_at_valid_indices(self):
        for val in [1, 2, 3]:
            self.ll.push_front(val)  # List = [3,2,1]
        self.assertEqual(self.ll.value_at(0), 3)
        self.assertEqual(self.ll.value_at(1), 2)
        self.assertEqual(self.ll.value_at(2), 1)

    def test_value_at_invalid_index_raises(self):
        with self.assertRaises(IndexError):
            self.ll.value_at(0)
        self.ll.push_front(99)
        with self.assertRaises(IndexError):
            self.ll.value_at(1)  # Only index 0 is valid

    # --- pop_front() tests ---
    def test_pop_front_single_element(self):
        self.ll.push_front(42)
        popped = self.ll.pop_front()
        self.assertEqual(popped, 42)
        self.assertTrue(self.ll.is_empty())
        self.assertEqual(self.ll.size(), 0)

    def test_pop_front_multiple_elements(self):
        for val in [5, 10, 15]:
            self.ll.push_front(val)  # [15,10,5]
        popped1 = self.ll.pop_front()
        self.assertEqual(popped1, 15)
        self.assertEqual(self.ll.front(), 10)
        popped2 = self.ll.pop_front()
        self.assertEqual(popped2, 10)
        self.assertEqual(self.ll.front(), 5)
        self.assertEqual(self.ll.size(), 1)

    def test_pop_front_empty_list_raises(self):
        with self.assertRaises(Exception):
            self.ll.pop_front()

    # --- front() tests ---
    def test_front_empty_list_raises(self):
        with self.assertRaises(Exception):
            self.ll.front()


class TestLinkedListPushPopBack(unittest.TestCase):
    def setUp(self):
        self.lst = LinkedList()

    # 1. Normal insertion and retrieval
    def test_push_and_back(self):
        self.lst.push_back(10)
        self.lst.push_back(20)
        self.lst.push_back(30)
        self.assertEqual(self.lst.back(), 30)
        self.assertEqual(self.lst.size(), 3)

    # 2. Single-element list
    def test_single_element_back(self):
        self.lst.push_back(42)
        self.assertEqual(self.lst.back(), 42)
        popped = self.lst.pop_back()
        self.assertEqual(popped, 42)
        self.assertTrue(self.lst.is_empty())

    # 3. Empty list edge case
    def test_pop_back_empty_list(self):
        with self.assertRaises(Exception):
            self.lst.pop_back()
        with self.assertRaises(Exception):
            self.lst.back()

    # 4. Multiple sequential operations
    def test_push_pop_back_sequence(self):
        data = [1, 2, 3, 4, 5]
        for item in data:
            self.lst.push_back(item)
        self.assertEqual(self.lst.back(), 5)
        self.assertEqual(self.lst.size(), 5)

        self.assertEqual(self.lst.pop_back(), 5)
        self.assertEqual(self.lst.pop_back(), 4)
        self.assertEqual(self.lst.size(), 3)
        self.assertEqual(self.lst.back(), 3)

        # add again after popping
        self.lst.push_back(99)
        self.assertEqual(self.lst.back(), 99)
        self.assertEqual(self.lst.size(), 4)

    # 5. Stress test with large input
    def test_large_push_back(self):
        n = 10000
        for i in range(n):
            self.lst.push_back(i)
        self.assertEqual(self.lst.back(), n - 1)
        self.assertEqual(self.lst.size(), n)

        # pop some elements
        for _ in range(100):
            self.lst.pop_back()
        self.assertEqual(self.lst.size(), n - 100)
        self.assertEqual(self.lst.back(), n - 101)

    # 6. Type and value diversity
    def test_push_back_varied_types(self):
        self.lst.push_back("apple")
        self.lst.push_back(3.14)
        self.lst.push_back(True)
        self.lst.push_back(None)
        self.assertEqual(self.lst.back(), None)
        self.assertEqual(self.lst.size(), 4)

        self.lst.pop_back()
        self.assertEqual(self.lst.back(), True)


if __name__ == "__main__":
    unittest.main()
