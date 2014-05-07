'''
A hash table (also hash map) is a data structure used to implement an *associative array*, a structure that can map keys to values. 
A hash table uses a hash function to compute an index (transforming a key into a _fixed_sized_ construct) into an array of buckets or slots, from which the correct value can be found.

Ideally, the hash function will assign each key to a unique bucket, but this situation is rarely achievable in practice (usually some keys will hash to the same bucket). Instead, most hash table designs assume that hash collisions—different keys that are assigned by the hash function to the same bucket—will occur and must be accommodated in some way.

In a well-dimensioned hash table, the average cost (number of instructions) for each lookup is independent of the number of elements stored in the table. Many hash table designs also allow arbitrary insertions and deletions of key-value pairs, at (amortized[2]) constant average cost per operation.[3][4]
'''

import itertools

class HashTable(object):
    class Bucket(object):
        __slots__ = ['item']
        def __init__(self, item):
            self.item = item
        def insert(self, item):
            self.item = item
        def search_by_key(self, key):
            return self.item[1]
        def __len__(self):
            return 1
        def __eq__(self, other):
            if self.item != other.item:
                return False
            return True
        def __iter__(self):
            return iter([self.item])

    RESOLUTION_OVERWRITE = 0
    RESOLUTION_CHAINING = 1
    RESOLUTION_OPEN_ADDRESING = 2

    @staticmethod
    def validate_container(container_type):
        return 'search_by_key' in vars(container_type) and 'insert' in vars(container_type) and 'delete' in vars(container_type)

    def __init__(self, container_type=Bucket, size=64, resolution=RESOLUTION_OVERWRITE, hash_function=hash):
        if resolution != HashTable.RESOLUTION_OVERWRITE:
            if not hasattr(container_type, '__dict__') or not HashTable.validate_container(container_type):
                raise ValueError('container_type must be a valid container')

        self.container_type = container_type
        self.size = size
        self.arr = [None]*size
        self.resolution = resolution
        self.hash_function = hash_function

    def i(self, key):
        return self.hash_function(key) % self.size

    def insert(self, key, value):
        i = self.i(key)

        if self.arr[i] is None:
            self.arr[i] = self.container_type((key,value))
        else:
            self.arr[i].insert((key,value))

    def search(self, key):
        i = self.i(key)
        return self.arr[i].search_by_key(key) if self.arr[i] is not None else None

    def delete(self, key):
        i = self.i(key)
        if len(self.arr[i]) == 1:
            self.arr[i] = None
        else:
            self.arr[i] = self.arr[i].delete((key, self.arr[i].search_by_key(key)))

    def __iter__(self):
        return iter(itertools.chain.from_iterable([x for x in self.arr if x is not None]))

    def __getitem__(self, key):
        return self.search(key)

    def __setitem__(self, key, value):
        return self.insert(key, value)
