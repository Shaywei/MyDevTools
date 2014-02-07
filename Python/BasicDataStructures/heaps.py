class LinkedList(object):
    __slots__ = ['_heap']

    def __init__(self, comparator=<):
        self._heap = list()
        
    def insert(self, item):
        raise NotImplemented()

    def search(self, item):
        raise NotImplemented()

    def delete(self, item):
        raise NotImplemented()

    # For HashTable
    def search_by_key(self, key):
        raise NotImplemented()

    def _bubbleup(self):
        raise NotImplemented()

    def _bubbledown(self):
        raise NotImplemented()

    def extract_min(self):
        raise NotImplemented()        

    def __len__(self):
        return len(self._heap)

    def __eq__(self, other):
        return self._heap == other._heap

    def __ne__(self, other):
        return not self.__eq__(other)

    def __iter__(self):
        return iter(self._heap)

    def __str__(self):
        return str(self._heap)

    def __repr__(self):
        return "%r" % (self._heap)
