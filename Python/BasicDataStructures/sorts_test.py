import unittest
import random, operator, sys

from heaps import Heap, mergesort

def _factory(l):
    _h = Heap()
    for item in l:
        _h.insert(item)
    return _h

class TestHeap(unittest.TestCase):
    def test_insert_minimum_at_the_root(self):
        # Arrange
        h = Heap()

        # Act
        h.insert(6)
        h.insert(5)
        h.insert(3)
        h.insert(4)
        h.insert(2)
        h.insert(1)

        # Assert
        self.assertEqual(1, h._heap[0])
    
    def test_extract_root(self):
        # Arrange
        h = Heap()
        h.insert(6)
        h.insert(5)
        h.insert(3)
        h.insert(4)
        h.insert(2)
        h.insert(1)

        # Act
        root = h.extract_root()

        # Assert
        self.assertEqual(1, root)
        self.assertEqual(2, h._heap[0])

    def test__eq__when_equal(self):
        # Arrange
        h1 = _factory([1,2,3])
        h2 = _factory([1,2,3])

        #Assert
        self.assertTrue(h1 == h2)

    def test__eq__when_not_equal(self):
        # Arrange
        h1 = _factory([1,2,3])
        h2 = _factory([1,3,2])

        #Assert
        self.assertFalse(h1 == h2)

    def test_min_heap_sort(self):
        # Arrange        
        seed = random.randint(0, sys.maxint)
        myRand = random.Random(seed)
        l = [int(10000*myRand.random()) for x in xrange(10000)]

        # Act
        l_sorted = Heap.heapsort(l)

        # Assert
        self.assertEqual(sorted(l), l_sorted)

    def test_max_heap_sort(self):
        # Arrange
        seed = random.randint(0, sys.maxint)
        myRand = random.Random(seed)
        l = [int(10000*myRand.random()) for x in xrange(10000)]

        # Act
        l_sorted = Heap.heapsort(l, operator.gt)

        # Assert
        self.assertEqual(sorted(l, reverse=True), l_sorted)        

    def test_mergesort(self):
        # Arrange
        seed = random.randint(0, sys.maxint)
        myRand = random.Random(seed)
        r = 100000
        l = [int(r*myRand.random()) for x in xrange(r)]

        # Act
        mergesort(l, 0, r-1)

        # Assert
        self.assertEqual(sorted(l), l)        

if __name__ == '__main__':
    unittest.main()
