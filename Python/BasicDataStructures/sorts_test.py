import unittest
import random, operator, sys

from sorts import heapsort, mergesort, insertion_sort, quicksort, quicksort_inplace

class TestSorts(unittest.TestCase):
    def test_min_heapsort(self):
        # Arrange
        seed = random.randint(0, sys.maxint)
        myRand = random.Random(seed)
        l = [int(10000*myRand.random()) for x in xrange(10000)]

        # Act
        l_sorted = heapsort(l)

        # Assert
        self.assertEqual(sorted(l), l_sorted)

    def test_max_heapsort(self):
        # Arrange
        seed = random.randint(0, sys.maxint)
        myRand = random.Random(seed)
        l = [int(10000*myRand.random()) for x in xrange(10000)]

        # Act
        l_sorted = heapsort(l, operator.gt)

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

    def test_insertion_sort(self):
        # Arrange
        seed = random.randint(0, sys.maxint)
        myRand = random.Random(seed)
        r = 5000
        l = [int(r*myRand.random()) for x in xrange(r)]

        # Act + Assert
        self.assertEqual(sorted(l), insertion_sort(l))

    def test_quicksort(self):
        # Arrange
        seed = random.randint(0, sys.maxint)
        myRand = random.Random(seed)
        r = 100000
        l = [int(r*myRand.random()) for x in xrange(r)]

        # Act + Assert
        self.assertEqual(sorted(l), quicksort(l))

    def test_quicksort_inplace(self):
        # Arrange
        seed = random.randint(0, sys.maxint)
        myRand = random.Random(seed)
        r = 100000
        l = [int(r*myRand.random()) for x in xrange(r)]

        # Act
        quicksort_inplace(l)

        # Assert
        self.assertEqual(sorted(l), l)

if __name__ == '__main__':
    unittest.main()
