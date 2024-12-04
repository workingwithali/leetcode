class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        # Return the tree in pre-order for simplicity
        result = []
        def pre_order(node):
            if node:
                result.append(str(node.val))
                pre_order(node.left)
                pre_order(node.right)
            else:
                result.append("None")
        pre_order(self)
        return " -> ".join(result)

class Solution:
    def invert(self, root):
        if not root:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invert(root.left)
        self.invert(root.right)
        return root

# Create the tree
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

# Invert the tree
solution = Solution()
r = solution.invert(root)

# Print the result
print(r)
