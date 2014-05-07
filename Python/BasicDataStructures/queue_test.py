import unittest

from queue import Queue

def _factory(l):
    _q = Queue()
    for item in l:
        _q.push(item)
    return _q

class TestQueue(unittest.TestCase):
    def test_push_pop_single_element(self):
        # Arrange
        q = Queue()

        # Act
        q.push('a')

        # Assert
        self.assertEqual(1, len(q))
        self.assertEqual('a', q.pop())
        self.assertEqual(0, len(q))

    def test_push_pop_three_element(self):
        # Arrange
        q = Queue()

        # Act
        q.push('a')
        q.push('b')
        q.push('c')

        # Assert
        self.assertEqual(3, len(q))
        self.assertEqual('a', q.pop())
        self.assertEqual(2, len(q))

    def test_push_complex(self):
        # Arrange
        q = Queue()

        # Act
        q.push('a')
        q.push('b')
        q.push('c')
        q.pop()
        q.pop()
        q.pop()
        q.push('d')
        q.push('e')

        # Assert
        self.assertEqual(2, len(q))
        self.assertEqual('d', q.pop())
        self.assertEqual('e', q.pop())
        self.assertEqual(0, len(q))

    def test_pop_on_empty_queue_raises_ValueError(self):
        # Arrange
        q = Queue()

        # Act + Assert
        with self.assertRaises(ValueError):
            q.pop()

    def test__eq__when_equal1(self):
        # Arrange
        q1 = _factory([1,2,3])
        q2 = _factory([1,2,3])

        #Assert
        self.assertTrue(q1 == q2)

    def test__eq__when_equal2(self):
        # Arrange
        q1 = Queue()
        q2 = Queue()

        #Assert
        self.assertTrue(q1 == q2)

    def test__eq__when_not_equal(self):
        # Arrange
        q1 = _factory([1,2,3])
        q2 = _factory([1,3,2])

        #Assert
        self.assertFalse(q1 == q2)

    def test_to_list(self):
        q = _factory([1,2,3,4,5])
        self.assertEqual([1,2,3,4,5], q.to_list())

    def test_iteration(self):
        # Arrange
        q = _factory([1,2,3,4,5])

        # Act + Assert
        for item, i in zip(q, range(1,6)):
            self.assertEqual(item, i)

    def test__len__(self):
        # Arrange
        q = _factory([1,2,3,4,5])

        # Act + Assert
        self.assertEqual(5, len(q))
    def test__str__(self):
        # Arrange
        q = _factory([1,2,3,4,5])

        # Act + Assert
        self.assertEqual('5->4->3->2->1', str(q))

if __name__ == '__main__':
    unittest.main()

