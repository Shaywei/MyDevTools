import unittest

from linked_lists import LinkedList

def _factory(l):
    _l = LinkedList(l[0])
    for item in l[1:]:
        _l.insert(item)
    return _l

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_sanity(self):
        # Act
        l = LinkedList(1)

        # Assert
        self.assertEqual(1, l.item)
        self.assertEqual(None, l.next_l)

    def test_insert(self):
        # Arrange
        l = LinkedList(1)

        # Act
        l.insert(2)
        l.insert(3)

        # Assert
        self.assertEqual(1, l.item)
        self.assertEqual(2, l.next_l.item)
        self.assertEqual(3, l.next_l.next_l.item)
        self.assertEqual(None, l.next_l.next_l.next_l)

    def test_insert_illegal_type_raises_ValueError(self):
        # Arrange
        l = LinkedList(1)

        # Act + Assert
        with self.assertRaises(ValueError):
            l.insert('2')

    def test__eq__when_equal(self):
        # Arrange
        l1 = _factory([1,2,3])
        l2 = _factory([1,2,3])

        #Assert
        self.assertTrue(l1 == l2)

    def test__eq__when_not_equal(self):
        # Arrange
        l1 = _factory([1,2,3])
        l2 = _factory([1,3,2])

        #Assert
        self.assertFalse(l1 == l2)

    def test_search_contains_return_list(self):
        # Arrange
        l = _factory([1,2,3,4,5])
        expected = _factory([4,5])

        # Act
        actual = l.search(4)

        # Assert
        self.assertEqual(expected, actual)

    def test_search_not_contains_return_None(self):
        # Arrange
        l = _factory([1,2,3,4,5])

        # Act + Assert
        self.assertIsNone(l.search(6))

    def test_delete_list_item(self):
        # Arrange
        l = _factory([1,2,3,4,5])

        # Act
        LinkedList.delete_list(l, 3)

        # Assert
        self.assertEqual(_factory([1,2,4,5]), l)

    def test_delete_list_item_that_doesnt_exist_raise_value_error(self):
        # Arrange
        l = _factory([1,2,3,4,5])

        # Act + Assert
        with self.assertRaises(ValueError):
            LinkedList.delete_list(l, 6)

    def test_delete_item(self):
        # Arrange
        l = _factory([1,2,3,4,5])

        # Act
        l.delete_list(l, 3)

        # Assert
        self.assertEqual(_factory([1,2,4,5]), l)

    def test_delete_item_that_doesnt_exist_raise_value_error(self):
        # Arrange
        l = _factory([1,2,3,4,5])

        # Act + Assert
        with self.assertRaises(ValueError):
            l.delete_list(l, 6)

    def test_to_list(self):
        l = _factory([1,2,3,4,5])
        self.assertEqual([1,2,3,4,5], l.to_list())

    def test_iteration(self):
        # Arrange
        l = _factory([1,2,3,4,5])

        # Act + Assert				

        for item, i in zip(l, range(1,6)):
            self.assertEqual(item, i)

    def test__str__(self):
        # Arrange
        l = _factory([1,2,3,4,5])

        # Act + Assert
        self.assertEqual('1->2->3->4->5', str(l))

    def test__len__(self):
        # Arrange
        l = _factory([1,2,3,4,5])

        # Act + Assert
        self.assertEqual(5, len(l))

    def test__repr__(self):
        # Arrange
        l = _factory([1,2,3])

        # Act + Assert
        self.assertEqual('LinkedList(item=1, next_l=LinkedList(item=2, next_l=LinkedList(item=3, next_l=None)))', l.__repr__())


if __name__ == '__main__':
    unittest.main()

