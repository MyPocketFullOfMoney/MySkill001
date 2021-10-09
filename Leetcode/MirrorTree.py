
from typing import List, Tuple


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Sultion:

    def mirrorTree(self,root:TreeNode) -> TreeNode:

        if not root:
            return root
        
        left = self.mirrorTree(root.left)
        right = self.mirrorTree(root.right)

        root.left,root.right = right,left
        return root



if __name__ == '__main__':

    root = TreeNode(4)

    left_child = TreeNode(2)
    right_child = TreeNode(3)

    root.left = left_child
    root.right = right_child
    print(root.val,root.left.val,root.right.val)

    test = Sultion()

    test.mirrorTree(root)

    print(root.val,root.left.val,root.right.val)

    

    