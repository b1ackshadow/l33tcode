from typing import Optional, List, NewType


type Result = list[int]
type Child = int | None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level = 0 # taking level 0 as the root node
        queue = [[root, level]]
        level += 1

        result = [root.val]
        while len(queue) > 0:
            node, n_level = queue.pop(0)
            children = []
            if node.left:
                children.append(node.left.val)
                queue.append([node.left, n_level + 1])
            if node.right:
                children.append(node.right.val)
                queue.append([node.right, n_level + 1])
            if children:
                if n_level + 1 <= len(result) - 1:  # if the level was alr created ? 
                    result[n_level + 1].extend(children)
                else:
                    result.append(children)

            level += 1


        return result
