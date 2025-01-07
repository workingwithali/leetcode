class Solution:
    def array(self,nums1,nums2):
        res = [set(),set()]
        for num1 in nums1:
            fount = True
            for num2 in nums2:
                if num1 == num2:
                    found = False
                    break
            if fount:
                res[0].add(num1)
                
            