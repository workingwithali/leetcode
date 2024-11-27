class solution:
    def swapping(self,head,k):
        cur = head
        for _ in range(k-1):
            cur = cur.next
        left