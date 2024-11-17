from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        # taking level 0 as the root node
        queue = [[root, 0]]

        result = [root.val]
        view = dict([0: root.val])
        while len(queue) > 0:
            node, n_level = queue.pop(0)

            if node.left:
                queue.append([node.left, n_level + 1])
                view[n_level + 1] = node.left.val

            if node.right:
                queue.append([node.right, n_level + 1])
                view[n_level + 1] = node.right.val

        return [ view[i] for i in range(len(view))]
