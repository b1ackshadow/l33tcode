from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root) != -1

    def dfs(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        l = 1 + self.dfs(root.left)
        r = 1 + self.dfs(root.right)

        if l == -1 or r == -1 or abs(l - r) > 1:
            return -1

        return max(l, r)

        


