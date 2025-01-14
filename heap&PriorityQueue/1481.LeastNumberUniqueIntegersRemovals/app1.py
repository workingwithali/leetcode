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
            


        return res