import heapq
class solution:
    def closepoint(self ,points):
        minheap = []
        for x,y in points:
            dist = (x**2)+(y**2)
            minheap.append([dist,x,y])
        heapq.heapify(minheap)
        res     

