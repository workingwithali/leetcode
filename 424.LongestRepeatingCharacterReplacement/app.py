class Solution:
    def longest(self, s, k):
        count = {}
        res = 0
        l = 0
        max_char = 0
        for r in range(len(s)):
            count [s[r]] =1 + count.get(s[r],0)
            if (r-l+1) - max(count.values())>k:
                count[s[l]] -=1
                l+=1



            res = max(res,r-l+1) 
        return res



sol = Solution()
s = "AABABBA"
k = 1
result = sol.longest(s,k)
print(result) 
