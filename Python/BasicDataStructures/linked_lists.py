class LinkedList(object):
    __slots__ = ['item', '_next']

    @staticmethod
    def delete_list(l, item):
        if l.item == item:
            return l._next

        link_to_delete = l.search(item)

        if link_to_delete is None:
            raise ValueError('item to be delete doesn\'t exist in list')
        else:
            pred_of_link_to_delete = l
            while pred_of_link_to_delete._next.item != item:
                pred_of_link_to_delete = pred_of_link_to_delete._next

            pred_of_link_to_delete._next = link_to_delete._next
            return l

    def __init__(self, item, _next=None):
        self.item = item
        self._next = _next

    def insert(self, item):
        if type(self.item) != type(item):
            raise ValueError('This list is of type: %s, you are trying to add an item of type: %s' % (type(self.item), type(item)))
        
        l = self
        while l._next is not None:
            l = l.next()

        l._next = LinkedList(item)

    def next(self):
        return self._next

    def search(self, item):
        if self.item == item:
            return self
        elif self._next is None:
            return None
        else:
            return self._next.search(item)

    def delete(self, item):
        if self.item == item:
            return self._next

        link_to_delete = self.search(item)

        if link_to_delete is None:
            raise ValueError('item to be delete doesn\'t exist in list')
        else:
            pred_of_link_to_delete = self
            while pred_of_link_to_delete._next.item != item:
                pred_of_link_to_delete = pred_of_link_to_delete._next

            pred_of_link_to_delete._next = link_to_delete._next
            return self

    def __eq__(self, other):
        if self.item != other.item or (self._next is None and other._next is not None) or (self._next is not None and other._next is None):
            return False
        elif self._next is None and other._next is None and self.item == other.item:
            return True
        else:
            return self.item == other.item and self._next == other._next

    def __ne__(self, other):
        return not self.__eq__(other)


    def __str__(self):
        s = ''
        p = self
        while p._next is not None:
            s += str(p.item) + '->'
            p = p._next
        return s + str(p.item)

    def __repr__(self):
        return "LinkedList(item=%r, _next=%r)" % (self.item ,self._next)
