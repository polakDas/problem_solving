# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.val = key

class Solution:
    def postorderTraversal(self, root) -> list[int]:
        if not root:
            return []
        pre = None
        stack = [root]
        cur = root.left
        result = []
        
        while True:
            if cur:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack[-1]
                if cur.right == None or cur.right == pre:
                    result.append(cur.val)
                    stack.pop()
                    pre = cur
                    cur = None
                else:
                    cur = cur.right
            else:
                break
                    
        return result

if __name__ == "__main__":
    root = Node(30)
    root.left = Node(20)
    root.right = Node(40)
    root.left.left = Node(15)
    root.left.right = Node(25)

    traversal = Solution()
    print(traversal.postorderTraversal(root=root))
