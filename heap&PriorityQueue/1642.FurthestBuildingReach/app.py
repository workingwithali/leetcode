import heapq
class solution:
    def build(self,heights,bricks,ladders):
        heap = [] #maxheap
        for i in range(len(heights)-1):
            diff = heights[i+1]-heights[i]
            if diff <= 0:
                continue
            bricks -= diff
            heapq.heappush(heap,-diff)
            if bricks < 0:
                if ladders == 0:
                    return i
                ladders -= 1
                bricks += -heapq.heappop(heap)
        return len(heap)-1
