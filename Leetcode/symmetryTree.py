# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.recur(root.left, root.right) if root else True 
    
    def recur(self,L:TreeNode,R:TreeNode) -> bool:
        if not L and not R: return True
        if not L or not R: return False
        if L.val != R.val: return False
        return self.recur(L.left,R.right) and self.recur(L.right,R.left)