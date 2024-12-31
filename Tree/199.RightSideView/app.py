from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Example tree
#      1
#     / \
#    2   3
root = TreeNode(1, TreeNode(2), TreeNode(3))

# Initialize deque
q = deque([root])

while q:
    node = q.popleft()  # Process the current node
    print(node.value)
    if node.left:
        q.append(node.left)  # Add left child to the queue
    if node.right:
        q.append(node.right)  # Add right child to the queue
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)