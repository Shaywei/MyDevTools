import unittest
import itertools
from functools import partial

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

    # Now that we tested insert(), we can use _factory!

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

    def test_min_max(self):
        for perm in itertools.permutations(range(5)):
            self.assertEqual(0, _factory(perm).min().item)
            self.assertEqual(4, _factory(perm).max().item)

    def test_inorder(self):
        b = _factory([2,1,3])
        self.assertEqual([1,2,3], b.inorder())

    def test_preorder(self):
        b = _factory([2,1,3])       
        self.assertEqual([2,1,3], b.preorder())

    def test_posorder(self):
        b = _factory([2,1,3])
        self.assertEqual([1,3,2], b.postorder())

    def test_search_parent(self):
        b = _factory([2,1,7,8,4,3,6,5])
        self.assertEqual(_factory([4,3,6,5]), b._search_parent(6))
        self.assertEqual(_factory([4,3,6,5]), b._search_parent(3))

    def test_delete_delete_childess_node(self):
        b = _factory([2,1,7,8,4,3,6,5])
        self.assertEqual(_factory([2,1,7,8,4,6,5]), b.delete(3))
    
    def test_delete_delete_node_with_one_child_left(self):
        b = _factory([2,1,7,8,4,3,6,5])
        self.assertEqual(_factory([2,1,7,8,4,3,5]), b.delete(6))

    def test_delete_delete_node_with_one_child_right(self):
        b = _factory([2,1,7,8,4,3,6,5,9])
        self.assertEqual(_factory([2,1,7,4,3,6,5,9]), b.delete(8))

    def test_delete_delete_node_with_two_children(self):
        b = _factory([2,1,7,8,4,3,6,5])
        self.assertEqual(_factory([2,1,7,8,5,3,6]), b.delete(4))

    def test_delete_delete_node_with_two_children_min_with_right_subtree(self):
        b = _factory([2,1,7,8,4,3,6,5,5.8,5.7,5.9])
        self.assertEqual(_factory([2,1,7,8,5,3,6,5.8,5.7,5.9]), b.delete(4))

    def test__repr__(self):
        # Arrange
        b = _factory([1,3,2])

        # Act + Assert
        self.assertEqual('BST(item=1, left=None, right=BST(item=3, left=BST(item=2, left=None, right=None), right=None))', b.__repr__())


if __name__ == '__main__':
    unittest.main()


