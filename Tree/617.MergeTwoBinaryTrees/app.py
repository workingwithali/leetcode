class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def MergeTree(self,root1,root2):
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.MergeTree(root1.left,root2.left)
        root1.left = self.MergeTree(root1.right,root2.right)
        return root1
    
solution = Solution()
root1 = [1,3,2,5]
root2 = [2,1,3,None,4,None,7]
result = solution.MergeTree(root1,root2)
print(result)