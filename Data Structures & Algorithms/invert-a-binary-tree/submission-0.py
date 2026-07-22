# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return None
        def solve(node):
            if node is None: return None
            temp = node.left
            node.left = node.right
            node.right = temp
            solve(node.left)
            solve(node.right)
        solve(root)
        return root