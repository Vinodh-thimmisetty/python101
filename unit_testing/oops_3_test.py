import unittest

from concepts.oops_3 import SimpleList, SortedList, IntList, SortedIntList


class MultipleInheritanceTests(unittest.TestCase):

    def test_simple_list(self):
        simple = SimpleList([11, 2, 32, 24, 52])
        self.assertEqual(len(simple.items), 5)
        simple.add(100)
        self.assertEqual(simple.size(), 6)
        simple.delete(100)
        self.assertFalse(simple.is_exists(100))
        simple.sort()
        self.assertEqual(simple.items, [2, 11, 24, 32, 52])
        simple.sort(True)
        self.assertEqual(simple.items, [52, 32, 24, 11, 2])

    def test_sorted_list(self):
        sorted_list = SortedList([11, 2, 32, 24, 52])
        self.assertTrue(issubclass(sorted_list.__class__, SimpleList))
        self.assertIsInstance(sorted_list, SortedList)
        self.assertListEqual(sorted_list.items, [2, 11, 24, 32, 52])
        sorted_list.add(28)
        self.assertListEqual(sorted_list.items, [2, 11, 24, 28, 32, 52])

    def test_int_list(self):
        int_list = IntList([11, 2, 32, 24, 52])
        self.assertTrue(issubclass(int_list.__class__, SimpleList))
        with self.assertRaises(TypeError):
            IntList([1, 2, "THREE", 4, 5])
        self.assertRaises(TypeError, int_list.add, "TEN")
        int_list.add(28)
        int_list.sort()
        self.assertListEqual(int_list.items, [2, 11, 24, 28, 32, 52])
        int_list.add(-42)
        int_list.add(0)
        int_list.sort(True)
        self.assertListEqual(int_list.items, [52, 32, 28, 24, 11, 2, 0, -42])

    def test_sorted_int_list(self):
        sorted_ints = SortedIntList([11, 2, 32, 24, 52])
        self.assertTrue(issubclass(sorted_ints.__class__, IntList))
        self.assertTrue(issubclass(sorted_ints.__class__, SimpleList))
        self.assertTrue(issubclass(sorted_ints.__class__, SortedList))
        with self.assertRaises(TypeError):
            IntList([1, 2, "THREE", 4, 5])
        self.assertRaises(TypeError, sorted_ints.add, "TEN")
        sorted_ints.add(28)
        self.assertListEqual(sorted_ints.items, [2, 11, 24, 28, 32, 52])
        sorted_ints.add(-42)
        sorted_ints.add(0)
        self.assertListEqual(sorted_ints.items, [-42, 0, 2, 11, 24, 28, 32, 52])
        sorted_ints.sort(True)
        self.assertEqual(sorted_ints.items, [52, 32, 28, 24, 11, 2, 0, -42])


if __name__ == '__main__':
    unittest.main()
