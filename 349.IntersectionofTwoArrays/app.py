class solution:
    def intersection(self,nums1,nums2):
        seen = set(nums1)
        res = []
        for n in nums2:
            if n in seen:
                res.append(n)
                seen.remove(n)
        return res
    
# solution = solution()
# nums1 = [1,2,2,1]
# nums2 = [2,2]
# result = solution.intersection(nums1,nums2)
# print(result)
