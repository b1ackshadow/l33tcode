from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.calcMaxDepth(root, 0)
    
    def calcMaxDepth(self, root, depth):
        if not root:
            return depth
        return max(self.calcMaxDepth(root.left, depth + 1), self.calcMaxDepth(root.right, depth + 1))


sol = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.left = TreeNode(7)


print(sol.maxDepth(root))
        
