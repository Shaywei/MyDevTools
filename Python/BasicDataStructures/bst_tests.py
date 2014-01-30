import unittest

from bst import BST

def _factory(l):
    _b = BST(l[0])
    for item in l[1:]:
        _b.insert(item)
    return _b



class TestBST(unittest.TestCase):
    
    def _check_node(self, node, item, left_child, right_child):
        self.assertEqual(item, node.item)
        if left_child is None:
            self.assertIsNone(node.left)
        else:
            self.assertEqual(left_child, node.left.item)

        if right_child is None:
            self.assertIsNone(node.right)
        else:
            self.assertEqual(right_child, node.right.item)

    def test_sanity(self):
        # Act
        b = BST(1)

        # Assert
        self.assertEqual(1, b.item)
        self.assertEqual(None, b.left)
        self.assertEqual(None, b.right)

    def test_insert_1(self):
        # Arrange + Act
        b = BST(1)
        b.insert(2)
        b.insert(3)

        # Assert
        self._check_node(b, 1, None, 2)
        self._check_node(b.right, 2, None, 3)
        self._check_node(b.right.right, 3, None, None)

    def test_insert_2(self):
        # Arrange + Act
        b = BST(1)
        b.insert(3)
        b.insert(2)

        # Assert
        self._check_node(b, 1, None, 3)
        self._check_node(b.right, 3, 2, None)
        self._check_node(b.right.left, 2, None, None)

    def test_insert_3(self):
        # Arrange + Act
        b = BST(2)
        b.insert(1)
        b.insert(3)

        # Assert
        self._check_node(b, 2, 1, 3)
        self._check_node(b.left, 1, None, None)
        self._check_node(b.right, 3, None, None)
    def test_insert_4(self):
        # Arrange + Act
        b = BST(2)
        b.insert(3)
        b.insert(1)

        # Assert
        self._check_node(b, 2, 1, 3)
        self._check_node(b.left, 1, None, None)
        self._check_node(b.right, 3, None, None)

    def test_insert_5(self):
        # Arrange + Act
        b = BST(3)
        b.insert(1)
        b.insert(2)

        # Assert
        self._check_node(b, 3, 1, None)
        self._check_node(b.left, 1, None, 2)
        self._check_node(b.left.right, 2, None, None)

    def test_insert_6(self):
        # Arrange + Act
        b = BST(3)
        b.insert(2)
        b.insert(1)

        # Assert
        self._check_node(b, 3, 2, None)
        self._check_node(b.left, 2, 1, None)
        self._check_node(b.left.left, 1, None, None)

    '''
    def test_insert_illegal_type_raises_ValueError(self):
        # Arrange
        b = BST(1)

        # Act + Assert
        with self.assertRaises(ValueError):
            b.insert('2')
    '''

    def test__eq__when_equal(self):
        # Arrange
        b1 = _factory([2,3,1])
        b2 = _factory([2,1,3])

        #Assert
        self.assertEqual(b1, b2)

    def test__eq__when_not_equal(self):
        # Arrange
        l1 = _factory([1,2,3])
        l2 = _factory([1,3,2])

        #Assert
        self.assertFalse(l1 == l2)


    def test_search_contains_return_list(self):
        # Arrange
        b = _factory([1,3,2,4])
        expected = _factory([3,4,2])

        # Act
        actual = b.search(3)

        # Assert
        self.assertEqual(expected, actual)

    def test_search_not_contains_return_None(self):
        # Arrange
        b = _factory([1,2,3,4,5])

        # Act + Assert
        self.assertIsNone(b.search(6))
    '''
    def test_traverse(self):
        # Arrange
        b = _factory([1,2,3,4,5])

        # Act
        b.delete_list(l, 3)

        # Assert
        self.assertEqual(_factory([1,2,4,5]), l)


    def test_delete_item(self):
        # Arrange
        b = _factory([1,2,3,4,5])

        # Act
        b.delete_list(l, 3)

        # Assert
        self.assertEqual(_factory([1,2,4,5]), l)

    def test_delete_item_that_doesnt_exist_raise_value_error(self):
        # Arrange
        b = _factory([1,2,3,4,5])

        # Act + Assert
        with self.assertRaises(ValueError):
            b.delete_list(l, 6)

    def test__repr__(self):
        # Arrange
        b = _factory([1,2,3])

        # Act + Assert
        self.assertEqual('BST(item=1, _next=BST(item=2, _next=BST(item=3, _next=None)))', b.__repr__())

    '''

if __name__ == '__main__':
    unittest.main()

