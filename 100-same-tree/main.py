from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        return self.dfs(p, q)


    def dfs(self, node1, node2):
        if node1 == node2 and node1 is None:
            return True

        if not node1 or not node2 or node1.val != node2.val:
            return False

        l = self.dfs(node1.left, node2.left) 
        r = self.dfs(node1.right, node2. right)

        return (l == r and l == True)

        

