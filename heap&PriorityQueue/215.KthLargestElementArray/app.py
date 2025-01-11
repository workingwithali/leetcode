import heapq
class solution:
    def largest(self,nums,k):
        return heapq.nlargest(k,nums)[-1]
    
solution =solution()