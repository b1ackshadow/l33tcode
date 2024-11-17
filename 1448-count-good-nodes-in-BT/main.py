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
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes_count = 0
        def dfs(root: Optional[TreeNode], max_ancestor: int):

            if not root:
                return 

            if root.val >= max_ancestor:
                nonlocal good_nodes_count 
                good_nodes_count +=  1
                max_ancestor = root.val

            dfs(root.left, max_ancestor)
            dfs(root.right, max_ancestor)

        dfs(root, root.val)
        return good_nodes_count




# Example usage:
# root = build_tree([3, 1, 4, 3, None, 1, 5])
# Now `root` is the root node of the binary tree built from the list

tests = [
    (build_tree([3,1,4,3,None,1,5]), 4),
    (build_tree([3,3,None,4,2]), 3),
    (TreeNode(1), 1)
]

sol = Solution()


for i, (test, want) in enumerate(tests):

    got = sol.goodNodes(test)
    assert got == want, f"Test case {i + 1} failed: got {got}, wanted {want}"
    print(f"Test case {i} passed with output {got}")
