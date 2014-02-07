import unittest

from heaps import Heap

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
        h.insert(2)
        h.insert(1)
        h.insert(3)

        # Assert
        self.assertEqual(1, h._heap[0])
    
    '''
    def test__eq__when_equal(self):
        # Arrange
        h1 = _factory([1,2,3])
        h2 = _factory([1,2,3])

        #Assert
        self.assertTrue(h1 == h2)
    \'''
    def test__eq__when_not_equal(self):
        # Arrange
        h1 = _factory([1,2,3])
        h2 = _factory([1,3,2])

        #Assert
        self.assertFalse(h1 == h2)
    \'''
    def test_search_contains_return_list(self):
        # Arrange
        h = _factory([1,2,3,4,5])
        expected = _factory([4,5])

        # Act
        actuah = h.search(4)

        # Assert
        self.assertEqual(expected, actual)
    \'''
    def test_search_not_contains_return_None(self):
        # Arrange
        h = _factory([1,2,3,4,5])

        # Act + Assert
        self.assertIsNone(h.search(6))
    \'''
    def test_delete_list_item(self):
        # Arrange
        h = _factory([1,2,3,4,5])

        # Act
        Heap.delete_list(l, 3)

        # Assert
        self.assertEqual(_factory([1,2,4,5]), l)
    \'''
    def test_delete_list_item_that_doesnt_exist_raise_value_error(self):
        # Arrange
        h = _factory([1,2,3,4,5])

        # Act + Assert
        with self.assertRaises(ValueError):
            Heap.delete_list(l, 6)
    \'''
    def test_delete_item(self):
        # Arrange
        h = _factory([1,2,3,4,5])

        # Act
        h.delete_list(l, 3)

        # Assert
        self.assertEqual(_factory([1,2,4,5]), l)
    \'''
    def test_delete_item_that_doesnt_exist_raise_value_error(self):
        # Arrange
        h = _factory([1,2,3,4,5])

        # Act + Assert
        with self.assertRaises(ValueError):
            h.delete_list(l, 6)
    \'''
    def test_to_list(self):
        h = _factory([1,2,3,4,5])
        self.assertEqual([1,2,3,4,5], h.to_list())
    \'''
    def test_iteration(self):
        # Arrange
        h = _factory([1,2,3,4,5])

        # Act + Assert				
        for item, i in zip(l, range(1,6)):
            self.assertEqual(item, i)
    \'''
    def test__str__(self):
        # Arrange
        h = _factory([1,2,3,4,5])

        # Act + Assert
        self.assertEqual('1->2->3->4->5', str(l))
    \'''
    def test__len__(self):
        # Arrange
        h = _factory([1,2,3,4,5])

        # Act + Assert
        self.assertEqual(5, len(l))
    \'''
    def test__repr__(self):
        # Arrange
        h = _factory([1,2,3])

        # Act + Assert
        self.assertEqual('Heap(item=1, next_l=Heap(item=2, next_l=Heap(item=3, next_l=None)))', h.__repr__())

    '''
if __name__ == '__main__':
    unittest.main()

