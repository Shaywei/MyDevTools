class BST(object):
    __slots__ = ['item', '_next']

    def __init__(self, item, _next=None):
        pass

    def insert(self, item):
        pass

    def search(self, item):
        pass

    def delete(self, item):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        return not self.__eq__(other)


    def __str__(self):
        '''
        s = ''
        p = self
        while p._next is not None:
            s += str(p.item) + '->'
            p = p._next
        return s + str(p.item)
        '''
        pass
        
    def __repr__(self):
        return "BST(item=%r, _next=%r)" % (self.item ,self._next)
