import unittest

from dsa import min_max_heap


class MinMaxHeapTestCase(unittest.TestCase):

    def test_heap_insertion(self):
        min_heap = min_max_heap.MinHeap()
        self.assertEqual(min_heap.heap, [])
        min_heap.push(100)
        self.assertEqual(min_heap.heap, [100])
        min_heap.push(200)
        self.assertEqual(min_heap.heap, [100, 200])
        min_heap.push(50)
        self.assertEqual(min_heap.heap, [50, 200, 100])
        min_heap.push(30)
        self.assertEqual(min_heap.heap, [30, 50, 100, 200])

    def test_heap_deletion(self):
        min_heap = min_max_heap.MinHeap()
        min_heap.push(100)
        min_heap.push(200)
        min_heap.push(50)
        min_heap.push(30)
        self.assertEqual(min_heap.heap, [30, 50, 100, 200])
        min_heap.poll()
        self.assertEqual(min_heap.heap, [50, 200, 100])

    def test_is_min_heap(self):
        min_heap = min_max_heap.MinHeap()
        min_heap.create_heap(items=[10,15,30,40,50,100,40])
        min_heap.display_tree()
        self.assertTrue(min_heap.is_heap())


if __name__ == '__main__':
    unittest.main()
