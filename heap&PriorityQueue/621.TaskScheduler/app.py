from collections import Counter, deque
import heapq
class solution:
    def task(self,tasks,n):
        count = Counter(tasks)
        maxheap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)
        time = 0
        q = deque()  # Stores tasks with their cooldown time
        
        while maxheap or q:
            time += 1
            if maxheap:
                cnt = 1 + heapq.heappop(maxheap)  # Increment because the heap stores negatives
                if cnt:
                    q.append([cnt, time + n])  # Correct cooldown time
            if q and q[0][1] == time:  # Check if a task's cooldown is complete
                heapq.heappush(maxheap, q.popleft()[0])
        
        return time