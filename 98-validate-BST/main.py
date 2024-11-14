from typing import Optional, List, Tuple
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    # basically need to do Inorder traversal. L -> Root -> R
        return self.inorder_traversal(root, float("-inf"), float('inf'))
    def inorder_traversal(self, root, mini, maxi) -> bool:

        if not root:
            return True

        if not (mini < root.val < maxi):
            return False

        l = root.left; r = root.right

        if l:
            l = self.inorder_traversal(l, mini, root.val)
        else:
            l = True

        if r:
            r = self.inorder_traversal(r, root.val, maxi)
        else:
            r = True

        return l and r





tests = [
    (build_tree([5,1,4,None,None,3,6]), False),
    (build_tree([2,1,3]), True),
    (build_tree([5,3,8,2,4,6,9]), True),
]

sol = Solution()


for i, (test, want) in enumerate(tests):

    got = sol.isValidBST(test)
    assert got == want, f"Test case {i + 1} failed: got {got}, wanted {want}"
    print(f"Test case {i} passed with output {got}")

