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

        where_to_search_next = self.left if item < self.item else self.right
        if where_to_search_next is None:
            return None
        return where_to_search_next.search(item)

    def min(self):
        m = self
        while m.left is not None:
            m = m.left
        return m

    def max(self):
        m = self
        while m.right is not None:
            m = m.right
        return m        

    def delete(self, item):
        pass

    def inorder(self, res=[]):
        if self.left is not None:
            self.left.inorder(res)

        res.append(self.item)

        if self.right is not None:
            self.right.inorder(res)

        return res

    def preorder(self, res=[]):
        res.append(self.item)

        if self.left is not None:
            self.left.preorder(res)

        if self.right is not None:
            self.right.preorder(res)

        return res

    def postorder(self, res=[]):
        if self.left is not None:
            self.left.preorder(res)

        if self.right is not None:
            self.right.preorder(res)

        res.append(self.item)

        return res

    def __eq__(self, other):
        if self.item != other.item:
            return False

        return self.left == other.left and self.right == other.right

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "BST(item=%r, left=%r, right=%r)" % (self.item, self.left, self.right)
