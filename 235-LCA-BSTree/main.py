class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p

        LCA = root

        return self.findLCA(root, p, q, LCA)

    def findLCA(self, root, p, q, LCA):
        if not root:
            return LCA

        if p.val <= root.val and q.val >= root.val:
            return root
        elif q.val < root.val:
            return self.findLCA(root.left, p, q, root.left)
        else:
            return self.findLCA(root.right, p, q, root.right)



