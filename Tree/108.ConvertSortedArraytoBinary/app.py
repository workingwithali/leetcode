class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortArray(self,nums):
        def helper(l,r):
            if l>r:
                return None
            m = (l+r)//2
            root = TreeNode(nums[m])
            root.left = helper(l,m-1)
            root.right = helper(m+1,r)
            return root
        return helper(0,len(nums)-1)

solution = Solution()
nums = [0,1,2,3,4,5]
result = solution.sortArray(nums)
print(result)
