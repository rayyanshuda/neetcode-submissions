# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # starting from root, there are 3 scenarios
        # 1. if value of p and q are both greater than root
        # both nodes are on the right branch
        # 2. if value of p and q are both less than root
        # both nodes are on the left branch
        # 3. if if its a split -> at LCA -> return node

        if p.val > root.val and q.val > root.val:
            root = root.right
        if p.val < root.val and q.val < root.val:
            root = root.left
        if (p.val >= root.val and q.val <= root.val) or (q.val >= root.val and p.val <= root.val):
            return root
        return self.lowestCommonAncestor(root, p, q)