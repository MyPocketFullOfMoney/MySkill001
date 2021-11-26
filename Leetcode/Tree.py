from typing import List, Tuple


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None





def createTree(root,data:List) -> TreeNode:
    
    
    if not data :
        return root
    elif data[0] != '#':
        root = TreeNode(data[0])
        data.pop(0)        
        root.left = createTree(root.left,data)
        root.right = createTree(root.right,data)
        return root
    else:
        data.pop(0)
        root = None
        return root



if __name__ == "__main__":
    
    root = None
    x = [4,2,'#','#',3,'#','#']
    tree = createTree(root,x)

    print(tree.val,tree.left.val,tree.right.val)