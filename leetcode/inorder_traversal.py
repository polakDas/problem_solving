# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root) -> list[int]:
        if not root:
            return []
        
        result = []
        stack = [root]
        current = root.left
        while True:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                result.append(current.val)
                current = current.right
            else:
                break
        return result