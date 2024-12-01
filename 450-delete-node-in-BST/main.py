from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def inOrderSuccessor(root):
            if not root:
                return root

            left = inOrderSuccessor(root.left)

            if left:
                return min(left.val, root.val)

            right = inOrderSuccessor(root.right)

            return min(right.val, root.val)
            

        def findAndDelete(root):
            if not root:
                return root

            if root.val == key:
                # leaf node
                if (not root.left) and (not root.right):
                    return None

                # left subtree only
                elif (not root.right):
                    return root.left
                # right subtree only
                elif (not root.left):
                    return root.right

                # right / left find Inorder successor that is the next Node in Inorer traversal from this node
                else:
                    return root.right
            
            elif key > root.val:
                root.right = findAndDelete(root.right)

            else:
                root.left = findAndDelete(root.left)

        return findAndDelete(root)


                

        


