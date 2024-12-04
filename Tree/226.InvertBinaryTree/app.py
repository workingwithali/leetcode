class TreeNode:
    def __init__(self,val=0,right=None,left=None) -> None:
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invert(self,root):
        if not root:
            return None
        temp = root.left  
        root.left = root.right
        root.right = temp
        self.invert(root.left)
        self.invert(root.right)
        return root

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)   
solution = Solution()
r = solution.invert(root)
print(r)
