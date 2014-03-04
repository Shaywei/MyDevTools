import operator

def heapsort(l, comparator=operator.lt):
    h = Heap(comparator)
    rng = xrange(len(l))
    for i in rng:
        h.insert(l.pop())
    for i in rng:
        l.append(h.extract_root())
    return l

class Heap(object):
    __slots__ = ['_heap', 'cmp']

    def __init__(self, comparator=operator.lt):
        self._heap = list()
        self.cmp = comparator

    def insert(self, item):
        i = len(self._heap)
        self._heap.append(item)
        self._bubbleup(i)

    def extract_root(self):
        if len(self._heap) == 1:
            return self._heap.pop()

        _root = self._heap[0]
        self._heap[0] = self._heap.pop()
        self._bubbledown(0)

        return _root

    # For HashTable
    def search_by_key(self, key):
        raise NotImplemented()

    def _bubbleup(self, index):
        parent_index = int((index - 1) / 2)
        if self._dominates(parent_index, index) or index == 0:
            return

        self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]
        self._bubbleup(parent_index)

    def _dominates(self, i, j):
        return self.cmp(self._heap[i], self._heap[j])

    def _child(self, i, _young=True):
        index = 2*i + 1 if _young else 2*i + 2
        return self._heap[index] if len(self._heap) - 1 >= index else None

    def _bubbledown(self, i):
        young_child, old_child = self._child(i), self._child(i, False)
        item = self._heap[i]

        if (young_child is None) or (old_child is None and self.cmp(item, young_child)) or (self.cmp(item, young_child) and self.cmp(item, old_child)):
            return

        dom_child_index = 2*i+1 if old_child is None or self.cmp(young_child, old_child) else 2*i + 2
        self._heap[i], self._heap[dom_child_index] = self._heap[dom_child_index], self._heap[i]
        self._bubbledown(dom_child_index)

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
