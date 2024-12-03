class TreeNode:
    def __init__(self,val=0,left= None, right=None) -> None:
        self.val = val
        self.left = left
        self.right =right
class Solution:
    def tree(self,root):
        res=[]
        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)
        postorder(root)
        return res

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
solution = Solution()
r = solution.tree(root)
print(r)