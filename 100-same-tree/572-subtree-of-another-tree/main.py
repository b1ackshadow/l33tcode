from re import sub
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs(root, subRoot)

    def isIdentical(self, node1, node2):
        if node1 == node2 and node1 is None:
            return True

        if not node1 or not node2 or node1.val != node2.val:
            return False

        l = self.dfs(node1.left, node2.left) 
        r = self.dfs(node1.right, node2. right)

        return (l == r and l == True)

    def dfs(self, root, subRoot):

        # if subRoot is empty 
        if not subRoot:
            return True

        # root empty but subROot isn't 
        if not root:
            return False

        if root.val == subRoot.val:
            # might be a subtree
            sameTree = self.isIdentical(root, subRoot)
            if sameTree:
                return True
        if root.val == subRoot.val and self.isIdentical(root.left, subRoot.left) and self.isIdentical(root.right, subRoot.right):
            return True
        
        # maybe it coule be elsewhere
        self.dfs(root.left, subRoot)
        self.dfs(root.right, subRoot)

        return False
            

