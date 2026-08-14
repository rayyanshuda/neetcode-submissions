# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # use pre-order so the first element is always root node
        code = []
        def convert(node):
            if node is None:
                code.append("#")
                return
            # first element is root node
            code.append(str(node.val))

            convert(node.left)
            convert(node.right)

            # join everything with commas
        convert(root)
        result = ",".join(code)
        return result # or code?


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = iter(data.split(","))
        
        def convert2():
            # get the next element in the sequence
            val = next(vals)
            if val == "#":
                return None
                
            node = TreeNode(int(val))
            node.left = convert2()
            node.right = convert2()
            return node
        
        return convert2()



