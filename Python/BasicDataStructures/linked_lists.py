class LinkedList(object):
    __slots__ = ['item', 'next_l']

    @staticmethod
    def from_list(l):
        _l = LinkedList(l[0])
        for item in l[1:]:
            _l.insert(item)
        return _l

    @staticmethod
    def delete_list(l, item):
        if l.item == item:
            return l.next_l

        link_to_delete = l.search(item)

        if link_to_delete is None:
            raise ValueError('item to be delete doesn\'t exist in list')
        else:
            pred_of_link_to_delete = l
            while pred_of_link_to_delete.next_l.item != item:
                pred_of_link_to_delete = pred_of_link_to_delete.next_l

            pred_of_link_to_delete.next_l = link_to_delete.next_l
            return l

    def __init__(self, item, next_l=None):
        self.item = item
        self.next_l = next_l

    def insert(self, item):
        if type(self.item) != type(item):
            raise ValueError('This list is of type: %s, you are trying to add an item of type: %s' % (type(self.item), type(item)))
        
        l = self
        while l.next_l is not None:
            l = l.next_l

        l.next_l = LinkedList(item)

    def to_list(self):
        ll = self
        l = [self.item]
        while ll.next_l:
            ll = ll.next_l
            l.append(ll.item)
        return l

    def search(self, item):
        if self.item == item:
            return self
        elif self.next_l is None:
            return None
        else:
            return self.next_l.search(item)

    def delete(self, item):
        if self.item == item:
            return self.next_l

        link_to_delete = self.search(item)

        if link_to_delete is None:
            raise ValueError('item to be delete doesn\'t exist in list')
        else:
            pred_of_link_to_delete = self
            while pred_of_link_to_delete.next_l.item != item:
                pred_of_link_to_delete = pred_of_link_to_delete.next_l

            pred_of_link_to_delete.next_l = link_to_delete.next_l
            return self

    # For HashTable
    def search_by_key(self, key):
        if self.item[0] == key:
            return self.item[1]
        elif self.next_l is None:
            return None
        else:
            return self.next_l.search_by_key(key)        

    def __len__(self):
        count = 1
        l = self
        while l.next_l is not None:
            count += 1
            l = l.next_l
        return count

    def __eq__(self, other):
        if self.item != other.item or (self.next_l is None and other.next_l is not None) or (self.next_l is not None and other.next_l is None):
            return False
        elif self.next_l is None and other.next_l is None and self.item == other.item:
            return True
        else:
            return self.item == other.item and self.next_l == other.next_l

    def __ne__(self, other):
        return not self.__eq__(other)

    def __iter__(self):
        return iter(self.to_list())

    def __str__(self):
        s = ''
        p = self
        while p.next_l is not None:
            s += str(p.item) + '->'
            p = p.next_l
        return s + str(p.item)

    def __repr__(self):
        return "LinkedList(item=%r, next_l=%r)" % (self.item ,self.next_l)
