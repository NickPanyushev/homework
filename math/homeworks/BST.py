class BST_Node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

    def __repr__(self):
        node = "Node %s left %s right %s " % (self.data, self.left, self.right)
        return node

    def get_data(self):
        return self.data

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def set_right(self, new_right):
        self.right = new_right

    def set_left(self, new_left):
        self.left = new_left


def build_BST(array, root=None):
    if not root:
        root = BST_Node(array[len(array) // 2])
    for i in array:
        if root.get_data() == i:
            continue
        if root.get_data() > i:
            if root.get_right() == None:
                root.set_right(BST_Node(i))
            else:
                build_BST([i], root.get_right())
        if root.get_data() < i:
            if root.get_left() == None:
                root.set_left(BST_Node(i))
            else:
                build_BST([i], root.get_left())
    return root


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tree = (build_BST(a))


def search(root, element):
    if root.get_data() == element:
        return root
    if root.get_data() > element:
        if root.get_right() == None:
            return None
        search(root.get_right(), element)
    if root.get_data() < element:
        if root.get_left() == None:
            return None
        return search(root.get_left(), element)

def max(root):
    if not root.get_left():
        return root.get_data()
    else:
        return max(root.get_left())

def min(root):
    if not root.get_right():
        return root.get_data()
    else:
        return min(root.get_right())



