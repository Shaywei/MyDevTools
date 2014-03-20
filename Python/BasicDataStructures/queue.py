from linked_lists import LinkedList

# To do, add better __str__ and __repr__, add support for max_size

class Queue(object):
    @staticmethod
    def from_list(l):
        _q = Queue()
        for item in l:
            _q.insert(item)
        return _q

    def __init__(self, max_size=None):
        self._ll = None
        self._head_of_queue = None
        self.max_size = max_size

    def push(self, item):
        if self._head_of_queue is None:
            self._ll = LinkedList(item)
            self._head_of_queue = self._ll
        else:
            self._head_of_queue.insert(item)
            self._head_of_queue = self._head_of_queue.next_l

    def to_list(self):
        return self._ll.to_list() if self._ll is not None else []

    def pop(self):
        if len(self) == 0:
            raise ValueError("Can't pop from an empty queue")

        ans = self._ll.item
        self._ll = self._ll.next_l
        if self._ll is None:
            self._head_of_queue = None
        return ans

    def __len__(self):
        return 0 if self._ll is None else len(self._ll)

    def __eq__(self, other):
        return self._ll == other._ll

    def __ne__(self, other):
        return not self.__eq__(other)

    def __iter__(self):
        return iter(self.to_list())

    def __str__(self):
        return '->'.join(map(str, self.to_list()[::-1]))
