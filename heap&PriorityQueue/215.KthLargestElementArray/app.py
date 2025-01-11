import heapq
class solution:
    def largest(self,nums,k):
        return heapq.nlargest(k,nums)[-1]
    
solution =solution()
nums = [3,2,1,5,6,4]
k = 2
r = solution.largest(nums,k)
print(r)