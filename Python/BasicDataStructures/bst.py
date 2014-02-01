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

    def _search_parent(self, item):
        if (self.left and self.left.item == item) or (self.right and self.right.item == item):
            return self
        
        where_to_search_next = self.left if item < self.item else self.right
        if where_to_search_next is None:
            return None
        return where_to_search_next._search_parent(item)

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
        node_to_be_deleted = self.search(item)
        if node_to_be_deleted is None:
            raise ValueError('Cant delete value that does not exist: %s' % (item))
        
        parent_of_node_to_be_deleted = self._search_parent(item)

        # Case 1 - childless 
        if node_to_be_deleted.left is None and node_to_be_deleted.right is None:
            if item < parent_of_node_to_be_deleted.item:
                parent_of_node_to_be_deleted.left = None
            else:
                parent_of_node_to_be_deleted.right = None

        # Case 2 - one child
        elif node_to_be_deleted.left is None and node_to_be_deleted.right is not None:
            BST._connect_nodes(parent_of_node_to_be_deleted, node_to_be_deleted.right)

        elif node_to_be_deleted.left is not None and node_to_be_deleted.right is None:
            BST._connect_nodes(parent_of_node_to_be_deleted, node_to_be_deleted.left)

        # Case 3 - two children - the left most child in the right subtree takes place.

        else:
            left_most_child_in_right_subtree = node_to_be_deleted.right.min()
            parent_of_left_most_child_in_right_subtree = self._search_parent(left_most_child_in_right_subtree.item)

            node_to_be_deleted.item = left_most_child_in_right_subtree.item
            parent_of_left_most_child_in_right_subtree.left = left_most_child_in_right_subtree.right

        return self

    def inorder(self):
        return self._traverse('inorder')

    def preorder(self):
        return self._traverse('preorder')

    def postorder(self):
        return self._traverse('postorder')

    def _traverse(self, how, res=None):
        if res is None:
            res = []

        if how == 'preorder':
            res.append(self.item)

        if self.left is not None:
            self.left._traverse(how, res)

        if how == 'inorder':
            res.append(self.item)

        if self.right is not None:
            self.right._traverse(how, res)

        if how == 'postorder':
            res.append(self.item)

        return res

    def __eq__(self, other):
        if self.item != other.item:
            return False

        return self.left == other.left and self.right == other.right

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return str(self.preorder())

    def __repr__(self):
        return "BST(item=%r, left=%r, right=%r)" % (self.item, self.left, self.right)

    @staticmethod
    def _connect_nodes(parent_node, child_node):
        if child_node.item < parent_node.item:
            parent_node.left = child_node
        else:
            parent_node.right = child_node