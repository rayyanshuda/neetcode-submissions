# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case: check if both trees exist? (not None)
        # walk through root until i find where subroot exists i think?
        # only start checking if subroot exists, until i've found the head node of subroot in root
        # after finding it
        # same thing as the question "binary same tree"

        # cannot have a subroot of a tree that doesn't exist
        if root is None:
            return False
        
        if subRoot is None and root:
            return True
        
        if self.isSametree(root, subRoot):
            return True

        # recursive step
        # traverse until root val is equal to subroot head val
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right

    def isSametree(self, p, q):
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False
        
        #third base: both of them exist: check value
        if p.val != q.val:
            return False

        left = self.isSametree(p.left, q.left)
        right = self.isSametree(p.right, q.right)

        return left and right
