class solution:
    def remove(self, head,n):
        N =0 
        cur = head
        while cur:
            N+=1
            cur = cur.next
        remove = N-n
        if remove ==0:
            return head.next
        for i in range(N-1):
            if (i+1)==remove:
                cur.nex?t = cur.next.next
                break
            cur = cur.next
        return head
