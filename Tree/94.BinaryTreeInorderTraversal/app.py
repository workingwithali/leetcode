class TreeNode:
    def __init__(self,val=0,left=None,right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree(self,root):
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root) 
        return res 

Solution = Solution()
root = [1,None,2,3]
r =Solution.tree(root)
print(r)