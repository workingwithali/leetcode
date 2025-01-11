import heapq
class solution:
    def closepoint(self ,points,k):
        minheap = []
        for x,y in points:
            dist = (x**2)+(y**2)
            minheap.append([dist,x,y])
        heapq.heapify(minheap)
        res  = []
        while k > 0:
            dist , x ,y = heapq.heappop(minheap)
            res.append([x,y])
            k -=1
        return res
    
solution = solution()
points = [[1,3],[-2,2]]
k = 1
r = solution.closepoint(points,k)
print(r)

