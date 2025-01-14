from collections import Counter
import heapq
class Solution:
    def freq(self,arr,k):
        freq = Counter(arr)
        heap = list(freq)
        heapq.heapify(heap)
        res = len(heap)
        while k > 0 and heap:
            f = heapq.heappop(heap)
            if k >= f:
                k -= f
                res -= 1
        return res
sol = Solution()
arr = [4,3,1,1,3,3,2]
k = 3
r 
