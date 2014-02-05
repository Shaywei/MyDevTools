import unittest
import itertools
from functools import partial

from hash_tables import HashTable
from linked_lists import LinkedList
def _factory(l):
    '''_b = BST(l[0])
    for item in l[1:]:
        _b.insert(item)
    return _b'''
    pass



class TestHashTable(unittest.TestCase):
    
    def test_init_container_type_must_have_search_insert_delete_if_resolution_is_not_overwrite(self):
        # Arrange
        class Foo():
            def insert():
                pass
            def search():
                pass

        # Act + Assert

        with self.assertRaises(ValueError):
            ht = HashTable(container_type='s', resolution=HashTable.RESOLUTION_CHAINING)

        with self.assertRaises(ValueError):
            ht = HashTable(container_type=Foo, resolution=HashTable.RESOLUTION_CHAINING)


    def test_init_sanity(self):
        # Arrange
        expected_size = 1024

        # Act
        ht = HashTable(container_type=LinkedList, size=expected_size, resolution=HashTable.RESOLUTION_CHAINING)

        # Arrange
        self.assertEqual((expected_size, LinkedList, HashTable.RESOLUTION_CHAINING, hash), (len(ht.arr), ht.container_type, ht.resolution, ht.hash_function))

    def test_insert_resolution_overwrite(self):
        # Arrange
        key = 'key'
        value = 'value'
        ht = HashTable()        
        i = ht.i(key)

        # Act
        ht.insert(key, value)

        # Assert
        self.assertEqual(value, ht.arr[i])

    def test_insert_resolution_chaning_no_collision(self):
        # Arrange
        key = 'key'
        value = 'value'
        ht = HashTable(container_type=LinkedList, resolution=HashTable.RESOLUTION_CHAINING)        
        i = ht.i(key)

        # Act
        ht.insert(key, value)

        # Assert
        self.assertEqual(LinkedList((key,value)), ht.arr[i])

    def test_insert_resolution_overwrite_overwrites(self):
        # Arrange
        key = 'key'
        value = 'value'
        value2 = 'value2'
        ht = HashTable()        
        i = ht.i(key)

        # Act
        ht.insert(key, value)
        ht.insert(key, value2)

        # Assert
        self.assertEqual(value2, ht.arr[i])

    def test_insert_resolution_chaning_with_collision_chains(self):
        # Arrange
        key = 'key'
        value = 'value'
        value2 = 'value2'
        ht = HashTable(container_type=LinkedList, resolution=HashTable.RESOLUTION_CHAINING)        
        i = ht.i(key)

        # Act
        ht.insert(key, value)
        ht.insert(key, value2)

        # Assert
        self.assertEqual(LinkedList((key,value), next_l=LinkedList((key,value2))), ht.arr[i])

    def test_search_resolution_overwrite(self):
        # Arrange
        key = 'key'
        value = 'value'
        ht = HashTable()        
        ht.insert(key, value)

        # Act + Assert
        self.assertEqual(value, ht.search(key))

    def test_search_resolution_chaning_without_collision(self):
        # Arrange
        key = 'key'
        value = 'value'
        ht = HashTable(container_type=LinkedList, resolution=HashTable.RESOLUTION_CHAINING)
        ht.insert(key, value)

        # Act + Assert
        self.assertEqual(value, ht.search(key))

    def test_search_resolution_chaning_with_collision(self):
        # Arrange
        key = 'key'
        value = 'value'
        key2 = 'key2'
        value2 = 'value2'
        ht = HashTable(container_type=LinkedList, resolution=HashTable.RESOLUTION_CHAINING, hash_function=lambda x: 1)
        ht.insert(key, value)
        ht.insert(key2, value2)

        # Act + Assert
        self.assertEqual((value, value2), (ht.search(key), ht.search(key2)))

    def test_delete_resolution_overwrite(self):
        # Arrange
        key = 'key'
        value = 'value'
        ht = HashTable()        
        ht.insert(key, value)

        # Act
        ht.delete(key)

        # Assert
        self.assertIsNone(ht.search(key))

    def test_delete_resolution_chaning_without_collision(self):
        return
        # Arrange
        key = 'key'
        value = 'value'
        ht = HashTable(container_type=LinkedList, resolution=HashTable.RESOLUTION_CHAINING)
        ht.insert(key, value)

        # Act
        ht.delete(key)

        # Assert
        self.assertIsNone(ht.search(key))

    def test_delete_resolution_chaning_with_collision(self):
        # Arrange
        key = 'key'
        value = 'value'
        key2 = 'key2'
        value2 = 'value2'
        ht = HashTable(container_type=LinkedList, resolution=HashTable.RESOLUTION_CHAINING, hash_function=lambda x: 1)
        ht.insert(key, value)
        ht.insert(key2, value2)

        # Act
        ht.delete(key)

        # Assert
        self.assertIsNone(ht.search(key))

if __name__ == '__main__':
    unittest.main()


