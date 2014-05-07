import unittest

from trie import Trie

class TestTrie(unittest.TestCase):
    '''
    def test_make_trie(self):
        # Arrange + Act
        t = Trie.make_trie(['in', 'inn', 'ten', 'tea', 'to'])

        # Assert
        self.assertEqual({'t': {'e': {'n': {'_EOW': '_EOW'}\
                                      'a': {'_EOW': '_EOW'} }\
                                'o': {'_EOW': '_EOW'} }\
                          'i': {'n': {'_EOW': '_EOW', 'n': {'_EOW': '_EOW'} }}
  '''

    def test_make_trie(self):
        # Arrange + Act
        t = Trie.make_trie(['tea'])

        # Assert

'''
    def test_insert_2(self):
        # Arrange + Act
        t = Trie(1)
        t.insert(3)
        t.insert(2)

        # Assert
        self._check_node(b, 1, None, 3)
        self._check_node(t.right, 3, 2, None)
        self._check_node(t.right.left, 2, None, None)

    def test_insert_3(self):
        # Arrange + Act
        t = Trie(2)
        t.insert(1)
        t.insert(3)

        # Assert
        self._check_node(b, 2, 1, 3)
        self._check_node(t.left, 1, None, None)
        self._check_node(t.right, 3, None, None)
    def test_insert_4(self):
        # Arrange + Act
        t = Trie(2)
        t.insert(3)
        t.insert(1)

        # Assert
        self._check_node(b, 2, 1, 3)
        self._check_node(t.left, 1, None, None)
        self._check_node(t.right, 3, None, None)

    def test_insert_5(self):
        # Arrange + Act
        t = Trie(3)
        t.insert(1)
        t.insert(2)

        # Assert
        self._check_node(b, 3, 1, None)
        self._check_node(t.left, 1, None, 2)
        self._check_node(t.left.right, 2, None, None)

    def test_insert_6(self):
        # Arrange + Act
        t = Trie(3)
        t.insert(2)
        t.insert(1)

        # Assert
        self._check_node(b, 3, 2, None)
        self._check_node(t.left, 2, 1, None)
        self._check_node(t.left.left, 1, None, None)

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
        t = _factory([1,3,2,4])
        expected = _factory([3,4,2])

        # Act
        actual = t.search(3)

        # Assert
        self.assertEqual(expected, actual)

    def test_search_not_contains_return_None(self):
        # Arrange
        t = _factory([1,2,3,4,5])

        # Act + Assert
        self.assertIsNone(t.search(6))

    def test_min_max(self):
        for perm in itertools.permutations(range(5)):
            self.assertEqual(0, _factory(perm).min().item)
            self.assertEqual(4, _factory(perm).max().item)

    def test_inorder(self):
        t = _factory([2,1,3])
        self.assertEqual([1,2,3], t.inorder())

    def test_preorder(self):
        t = _factory([2,1,3])       
        self.assertEqual([2,1,3], t.preorder())

    def test_posorder(self):
        t = _factory([2,1,3])
        self.assertEqual([1,3,2], t.postorder())

    def test_search_parent(self):
        t = _factory([2,1,7,8,4,3,6,5])
        self.assertEqual(_factory([4,3,6,5]), t._search_parent(6))
        self.assertEqual(_factory([4,3,6,5]), t._search_parent(3))

    def test_delete_delete_childess_node(self):
        t = _factory([2,1,7,8,4,3,6,5])
        self.assertEqual(_factory([2,1,7,8,4,6,5]), t.delete(3))
    
    def test_delete_delete_node_with_one_child_left(self):
        t = _factory([2,1,7,8,4,3,6,5])
        self.assertEqual(_factory([2,1,7,8,4,3,5]), t.delete(6))

    def test_delete_delete_node_with_one_child_right(self):
        t = _factory([2,1,7,8,4,3,6,5,9])
        self.assertEqual(_factory([2,1,7,4,3,6,5,9]), t.delete(8))

    def test_delete_delete_node_with_two_children(self):
        t = _factory([2,1,7,8,4,3,6,5])
        self.assertEqual(_factory([2,1,7,8,5,3,6]), t.delete(4))

    def test_delete_delete_node_with_two_children_min_with_right_subtree(self):
        t = _factory([2,1,7,8,4,3,6,5,5.8,5.7,5.9])
        self.assertEqual(_factory([2,1,7,8,5,3,6,5.8,5.7,5.9]), t.delete(4))

    def test__repr__(self):
        # Arrange
        t = _factory([1,3,2])

        # Act + Assert
        self.assertEqual('Trie(item=1, left=None, right=Trie(item=3, left=Trie(item=2, left=None, right=None), right=None))', t.__repr__())
'''

if __name__ == '__main__':
    unittest.main()


