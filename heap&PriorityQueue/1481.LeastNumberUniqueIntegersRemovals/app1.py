from collections import Counter
import heapq
class Solution:
    def freq(self,arr):
        freq = Counter(arr)
        heap = list(freq)
        heapq.heapify(heap)
        res = len(heap)

        return res