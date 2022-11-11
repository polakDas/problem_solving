# class Node:
#     def __init__(self, data: int, right = None, left = None):
#         self.data = data
#         self.right = None
#         self.left = None

# def morris_traversal(root) -> list[int]:
#     '''In-order traversal function'''

#     result = []
#     current = root

#     while current:
#         if not current.left:
#             result.append(current.data)
#             current = current.right
#         else:
#             pre = current.left
#             while pre.right and pre.right is not current:
#                 pre = pre.right
#             if not pre.right:
#                 pre.right = current
#                 current = current.left
#             else:
#                 pre.right = None
#                 result.append(current.data)
#                 current = current.right
#     return result

# if __name__ == "__main__":
#     root = Node(1,
#             right=Node(3),
#             left=Node(2,
#                 left=Node(4),
#                 right=Node(5))
#             )
#     print(morris_traversal(root=root))

# Python program to do Morris inOrder Traversal:
# inorder traversal without recursion and without stack


class Node:
	"""A binary tree node"""

	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


def morris_traversal(root):
	"""Generator function for
	iterative inorder tree traversal"""

	current = root

	while current is not None:

		if current.left is None:
			yield current.data
			current = current.right
		else:

			# Find the inorder
			# predecessor of current
			pre = current.left
			while pre.right is not None and pre.right is not current:
				pre = pre.right

			if pre.right is None:

				# Make current as right
				# child of its inorder predecessor
				pre.right = current
				current = current.left

			else:
				# Revert the changes made
				# in the 'if' part to restore the
				# original tree. i.e., fix
				# the right child of predecessor
				pre.right = None
				yield current.data
				current = current.right


# Driver code
"""
Constructed binary tree is
			1
		/ \
		2	 3
	/ \
	4	 5
"""
root = Node(1,
			right=Node(3),
			left=Node(2,
					left=Node(4),
					right=Node(5)
					)
			)

for v in morris_traversal(root):
	print(v, end=' ')

# This code is contributed by Naveen Aili
# updated by Elazar Gershuni
