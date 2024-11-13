from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:



def list_to_tree(lst: List[Optional[int]]) -> Optional[TreeNode]:
    if not lst:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in lst]
    for i in range(len(lst)):
        if nodes[i] is not None:
            if 2 * i + 1 < len(lst):
                nodes[i].left = nodes[2 * i + 1]
            if 2 * i + 2 < len(lst):
                nodes[i].right = nodes[2 * i + 2]
    return nodes[0]

test_cases = [
    ([1, 2, 3, 4, 5], 3),
    ([1, 2], 1),
    ([1, 2, 3, None, 4, None, 5, 6, None], 4),
    ([1, 2, None, 3, None, None, None, 4, 5], 3)
]

for root_input, expected_output in test_cases:
    root = list_to_tree(root_input)
    result = Solution().diameterOfBinaryTree(root)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

print("All test cases passed!")
