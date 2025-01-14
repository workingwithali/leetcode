class solution:
    def build(self,heights,bricks,ladders):
        heap = [] #maxheap
        for i in range(len(heights)-1):
            diff = heights[i+1]-heights[i]
            if diff <= 0:
                