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
