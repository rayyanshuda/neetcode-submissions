# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # pre order tells us what the root node is (first element)
        # everything to the left of that root node in inorder is in the left subtree
        # index using a hashmap
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        self.pre_index = 0

        def builder(left_index, right_index):
            if left_index > right_index:
                return None
            
            root_val = preorder[self.pre_index]
            root = TreeNode(root_val)
            self.pre_index += 1

            # find where root is in inorder
            mid = inorder_map[root_val]

            # build left and right subtrees recursively
            # everything left of mid goes to left subtree 
            # everything right of mid goes to right subtree

            root.left = builder(left_index, mid - 1)
            root.right = builder(mid + 1, right_index)
        
            return root
        
        return builder(0, len(inorder) - 1)


