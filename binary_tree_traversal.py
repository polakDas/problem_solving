class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.key = key

class Traversal:
    def preOrder(self, root) -> None:
        if root:
            print(root.key, end=" ")
            self.inOrder(root.left)
            self.inOrder(root.right)

    def inOrder(self, root) -> None:
        if root:
            self.inOrder(root.left)
            print(root.key, end=" ")
            self.inOrder(root.right)
        
    def postOrder(self, root) -> None:
        if root:
            self.inOrder(root.left)
            self.inOrder(root.right)
            print(root.key, end=" ")

# class Insertion:
#     def insert(self, keys):
#         for key in keys:
            

if __name__ == "__main__":
    root = Node(30)
    root.left = Node(20)
    root.right = Node(40)
    root.left.left = Node(15)
    root.left.right = Node(25)

    traverse = Traversal()
    traverse.preOrder(root=root)
    print()
    traverse.inOrder(root=root)
    print()
    traverse.postOrder(root=root)