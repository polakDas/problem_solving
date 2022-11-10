# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root) -> list[int]:
        if not root:
            return []
        result = []
        stack = [root]
        
        while stack:
            current = stack.pop()
            result.append(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
                
        return result
        
#         Recursive 

#         result = []
#         def preOrder(node):
#             if not node:
#                 return
#             result.append(node.val)
#             preOrder(node.left)
#             preOrder(node.right)
            
#         preOrder(root)
#         return result

        