
class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,val):
        if val < self.data:
            if self.left is None:
                self.left = BinaryTree(val)
            else:
                self.left.insert(val)
        elif val > self.data:
            if self.right is None:
                self.right = BinaryTree(val)
            else:
                self.right.insert(val)
        else:
            pass

    def remove(self, val):
        pass

    def inorderTraversal(self, root):
        ls = []
        if root:
            ls = self.inorderTraversal(root.left)
            ls.append(root.data)
            ls = ls + self.inorderTraversal(root.right)
        return ls
