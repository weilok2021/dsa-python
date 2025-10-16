import unittest
from dynamic_array import DynamicArray


# ------------------------ #
#  BASIC CONSTRUCTOR TESTS #
# ------------------------ #

class TestDynamicArrayInit(unittest.TestCase):
    def test_initial_capacity_and_size(self):
        arr = DynamicArray()
        self.assertEqual(arr.size(), 0)
        self.assertGreaterEqual(arr.capacity(), 16)
        self.assertTrue(arr.is_empty())

    def test_custom_capacity(self):
        arr = DynamicArray(8)
        self.assertEqual(arr.capacity(), 8)
        self.assertEqual(arr.size(), 0)


# ------------------------ #
#  PUSH / POP FUNCTIONALITY #
# ------------------------ #

class TestDynamicArrayPushPop(unittest.TestCase):
    def setUp(self):
        self.arr = DynamicArray()

    def test_push_adds_items_correctly(self):
        for i in range(5):
            self.arr.push(i)
        self.assertEqual(self.arr.to_list(), [0, 1, 2, 3, 4])
        self.assertEqual(self.arr.size(), 5)

    def test_push_triggers_resize_up(self):
        cap = self.arr.capacity()
        for i in range(cap + 1):
            self.arr.push(i)
        self.assertGreater(self.arr.capacity(), cap)

    def test_pop_removes_last_element(self):
        for i in range(4):
            self.arr.push(i)
        last = self.arr.pop()
        self.assertEqual(last, 3)
        self.assertEqual(self.arr.size(), 3)
        self.assertEqual(self.arr.to_list(), [0, 1, 2])

    def test_pop_from_empty_raises(self):
        with self.assertRaises(IndexError):
            self.arr.pop()


# ------------------------ #
#  INDEX ACCESS (at) TESTS #
# ------------------------ #

class TestDynamicArrayAccess(unittest.TestCase):
    def setUp(self):
        self.arr = DynamicArray()
        for i in range(5):
            self.arr.push(i)

    def test_valid_access(self):
        self.assertEqual(self.arr.at(0), 0)
        self.assertEqual(self.arr.at(4), 4)

    def test_out_of_bounds_access(self):
        with self.assertRaises(IndexError):
            self.arr.at(10)
        with self.assertRaises(IndexError):
            self.arr.at(-1)


# ------------------------ #
#   INSERT / PREPEND TESTS #
# ------------------------ #

class TestDynamicArrayInsert(unittest.TestCase):
    def setUp(self):
        self.a = DynamicArray()
        for i in [1, 2, 3, 4, 5]:
            self.a.push(i)

    def test_insert_at_start(self):
        self.a.insert(0, 99)
        self.assertEqual(self.a.to_list(), [99, 1, 2, 3, 4, 5])

    def test_insert_in_middle(self):
        self.a.insert(2, 77)
        self.assertEqual(self.a.to_list(), [1, 2, 77, 3, 4, 5])

    def test_insert_at_end(self):
        self.a.insert(self.a.size(), 55)
        self.assertEqual(self.a.to_list(), [1, 2, 3, 4, 5, 55])

    def test_insert_negative_index_raises(self):
        with self.assertRaises(IndexError):
            self.a.insert(-2, 10)

    def test_insert_beyond_end_raises(self):
        with self.assertRaises(IndexError):
            self.a.insert(self.a.size() + 1, 10)


# ------------------------ #
#        DELETE TESTS      #
# ------------------------ #

class TestDynamicArrayDelete(unittest.TestCase):
    def setUp(self):
        self.a = DynamicArray()
        for i in range(6):
            self.a.push(i)

    def test_delete_first(self):
        self.a.delete(0)
        self.assertEqual(self.a.to_list(), [1, 2, 3, 4, 5])

    def test_delete_middle(self):
        self.a.delete(3)
        self.assertEqual(self.a.to_list(), [0, 1, 2, 4, 5])

    def test_delete_last(self):
        self.a.delete(self.a.size() - 1)
        self.assertEqual(self.a.to_list(), [0, 1, 2, 3, 4])

    def test_delete_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.a.delete(999)

    def test_delete_on_empty_raises(self):
        b = DynamicArray()
        with self.assertRaises(IndexError):
            b.delete(0)

    def test_delete_triggers_resize_down(self):
        b = DynamicArray(8)
        for i in range(8):
            b.push(i)
        for _ in range(7):
            b.delete(0)
        self.assertEqual(b.capacity(), 4)


# ------------------------ #
#         REMOVE TESTS     #
# ------------------------ #

class TestDynamicArrayRemove(unittest.TestCase):
    def setUp(self):
        self.a = DynamicArray()
        for i in [1, 2, 3, 2, 4, 2, 5]:
            self.a.push(i)

    def test_remove_single_occurrence(self):
        self.a.remove(3)
        self.assertEqual(self.a.to_list(), [1, 2, 2, 4, 2, 5])

    def test_remove_multiple_occurrences(self):
        self.a.remove(2)
        self.assertEqual(self.a.to_list(), [1, 3, 4, 5])

    def test_remove_nonexistent_item(self):
        before = self.a.to_list()
        self.a.remove(99)
        self.assertEqual(self.a.to_list(), before)

    def test_remove_first_item(self):
        self.a.remove(1)
        self.assertEqual(self.a.to_list(), [2, 3, 2, 4, 2, 5])

    def test_remove_last_item(self):
        self.a.remove(5)
        self.assertEqual(self.a.to_list(), [1, 2, 3, 2, 4, 2])

    def test_remove_all_items(self):
        b = DynamicArray()
        for _ in range(3):
            b.push(7)
        b.remove(7)
        self.assertTrue(b.is_empty())

    def test_remove_from_empty(self):
        b = DynamicArray()
        b.remove(10)
        self.assertTrue(b.is_empty())


class TestDynamicArrayFind(unittest.TestCase):
    def setUp(self):
        self.a = DynamicArray()
        for i in [10, 20, 30, 40, 50]:
            self.a.push(i)

    def test_find_existing_item(self):
        self.assertEqual(self.a.find(30), 2)

    def test_find_first_occurrence(self):
        self.a.push(30)
        self.assertEqual(self.a.find(30), 2)

    def test_find_nonexistent_item(self):
        self.assertEqual(self.a.find(99), -1)

    def test_find_in_empty_array(self):
        b = DynamicArray()
        self.assertEqual(b.find(1), -1)
    

class TestDynamicArrayStress(unittest.TestCase):
    def test_large_number_of_appends_and_deletes(self):
        arr = DynamicArray()
        for i in range(1000):
            arr.push(i)
        self.assertEqual(arr.size(), 1000)

        for _ in range(990):
            arr.delete(0)
        self.assertLessEqual(arr.capacity(), 1024)  # ensures it shrinks

    def test_remove_then_append_pattern(self):
        arr = DynamicArray()
        for i in [1, 2, 3, 2, 4]:
            arr.push(i)
        arr.remove(2)
        arr.push(2)
        self.assertEqual(arr.to_list(), [1, 3, 4, 2])


class TestDynamicArrayIntegration(unittest.TestCase):
    def test_combined_operations(self):
        arr = DynamicArray()
        arr.push(10)
        arr.push(20)
        arr.insert(1, 15)
        arr.delete(0)
        arr.remove(20)
        arr.push(25)
        self.assertEqual(arr.to_list(), [15, 25])
        self.assertEqual(arr.size(), 2)



if __name__ == '__main__':
    unittest.main()
