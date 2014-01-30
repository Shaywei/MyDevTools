class BST(object):
    __slots__ = ['item', 'left', 'right']

    def __init__(self, item, _left=None, _right=None):
        self.item = item
        self.left = _left
        self.right = _right

    def insert(self, item):
        if item < self.item:
            if self.left is None:
                self.left = BST(item)
            else:
                self.left.insert(item)
        else:
            if self.right is None:
                self.right = BST(item)
            else:
                self.right.insert(item)

    def search(self, item):
        if self.item == item:
            return self

        elif item < self.item:
            if self.left is None:
                return None
            return self.left.search(item)
        else:
            if self.right is None:
                return None
            return self.right.search(item)


    def delete(self, item):
        pass

    def traverse(self):
        pass

    def __eq__(self, other):
        if self.item != other.item:
            return False

        return self.left == other.left and self.right == other.right

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "BST(item=%r, left=%r, right=%r)" % (self.item, self.left, self.right)
