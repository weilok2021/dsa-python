import unittest
import random
import math
from dynamic_array import DynamicArray


class TestDynamicArrayRandomized(unittest.TestCase):
    def setUp(self):
        random.seed(12345)  # reproducible randomness
        self.num_trials = 20
        self.ops_per_trial = 50000
        self.value_range = 1000

    def test_randomized_operations(self):
        for trial in range(self.num_trials):
            arr = DynamicArray()
            mirror = []

            for step in range(self.ops_per_trial):
                op = random.choice(["push", "pop", "insert", "delete", "remove", "find", "prepend"])
                # small probability of generating invalid input
                allow_invalid = random.random() < 0.05

                if op == "push":
                    val = random.randint(-self.value_range, self.value_range)
                    arr.push(val)
                    mirror.append(val)

                elif op == "pop":
                    if mirror:
                        val1 = arr.pop()
                        val2 = mirror.pop()
                        self.assertEqual(val1, val2)

                elif op == "insert":
                    val = random.randint(-self.value_range, self.value_range)
                    if mirror:
                        # sometimes insert out of bounds intentionally
                        index = random.randint(-2, len(mirror) + (2 if allow_invalid else 0))
                    else:
                        index = 0
                    try:
                        arr.insert(index, val)
                        mirror.insert(index, val)
                    except IndexError:
                        # both should reject invalid indices
                        self.assertTrue(index < 0 or index > len(mirror))

                elif op == "delete":
                    if mirror:
                        index = random.randint(-1, len(mirror) + (1 if allow_invalid else -1))
                        try:
                            arr.delete(index)
                            del mirror[index]
                        except IndexError:
                            self.assertTrue(index < 0 or index >= len(mirror))

                elif op == "remove":
                    if mirror:
                        val = random.choice(mirror + [99999] if allow_invalid else mirror)
                        try:
                            arr.remove(val)
                            mirror = [x for x in mirror if x != val]
                        except Exception:
                            # should not crash
                            pass

                elif op == "find":
                    if random.random() < 0.5:
                        val = random.randint(-self.value_range, self.value_range)
                    else:
                        val = random.choice(mirror) if mirror else random.randint(-10, 10)
                    result_arr = arr.find(val)
                    try:
                        result_list = mirror.index(val)
                    except ValueError:
                        result_list = -1
                    self.assertEqual(result_arr, result_list)

                elif op == "prepend":
                    val = random.randint(-self.value_range, self.value_range)
                    arr.prepend(val)
                    mirror.insert(0, val)

                # occasional invariant checks
                if step % 500 == 0:
                    self.assertEqual(arr.size(), len(mirror))
                    # Optional: check logical contents match
                    self.assertEqual(arr.to_list(), mirror)

                    # Invariant: capacity >= size always
                    self.assertGreaterEqual(arr.capacity(), arr.size())

                    # If your array shrinks dynamically:
                    if arr.size() > 0:
                        self.assertLessEqual(arr.size(), arr.capacity())

            # After each full trial, do final invariant check
            self.assertEqual(arr.to_list(), mirror)
            self.assertEqual(arr.size(), len(mirror))
            self.assertGreaterEqual(arr.capacity(), arr.size())
