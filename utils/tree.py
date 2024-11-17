from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or not values[0]:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while i < len(values):
        current = queue.pop(0)

        # Assign left child
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        # Assign right child
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:



tests = [
    (build_tree([3,1,4,None,2]), 1, 1),
    (build_tree([5,3,6,2,4,None,None,1]), 3, 3)
];



for i, (root, k, want) in enumerate(tests):

    got = sol.goodNodes(test)
    assert got == want, f"Test case {i + 1} failed: got {got}, wanted {want}"
    print(f"Test case {i} passed with output {got}")

