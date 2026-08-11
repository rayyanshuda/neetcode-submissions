# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case: both are empty -> They are the same
        if p is None and q is None:
            return True
            
        # base case: only one is empty -> They can't be the same
        if p is None or q is None:
            return False
        
        if p.val != q.val:
            return False

        else:
            # check that the left node p equals left node q
            left = self.isSameTree(p.left, q.left)
            # how do i compare the 2 nodes?
            right = self.isSameTree(p.right, q.right)


        return left and right
