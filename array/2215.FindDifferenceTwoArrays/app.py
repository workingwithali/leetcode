from typing import List

class Solution:
    def array(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = [set(), set()]
        for num1 in nums1:
            found = True
            for num2 in nums2:
                if num1 == num2:
                    found = False
                    break
            if found:
                res[0].add(num1)
        
        for num2 in nums2:
            found = True
            for num1 in nums1:
                if num1 == num2:
                    found = False
                    break
            if found:
                res[1].add(num2)
        
        return [list(res[0]), list(res[1])]

# Example usage
solution = Solution()
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
result = solution.array(nums1, nums2)
print(result)
