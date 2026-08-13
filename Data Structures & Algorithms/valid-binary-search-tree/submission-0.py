# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

    
        def boundary(node, minVal, maxVal):
            # base case
            # no root -> return true 
            if node is None:
                return True
            
            if node.val <= minVal or node.val >= maxVal:
                return False
            
            left_valid = boundary(node.left, minVal, node.val)
            right_valid = boundary(node.right, node.val, maxVal)

            return left_valid and right_valid
    
        return boundary(root, float('-inf'), float('inf'))
