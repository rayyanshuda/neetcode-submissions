# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
            
        # list to hold all the levels
        result = []
        
        # Initialize the queue with the root node inside it
        queue = deque([root])
        # level size is length of queue!!!
        # run loop while queue still has elements
        while queue:
            curr_lvl = []
            level_size = len(queue)
            while (level_size > 0):
                node = queue.popleft()
                curr_lvl.append(node.val)
                # add current nodes children in the queue (if they exist)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                level_size -= 1
            # add curr_level to result
            result.append(curr_lvl)
        return result
