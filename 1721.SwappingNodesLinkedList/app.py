class solution:
    def swapping(self,head,k):
        cur = head
        for _ in range(k-1):
            cur = cur.next
        left = cur
        right = head
        while cur.next:
            cur = cur.next
            right = right.next
        left.val , right.val = right.val , left.val
        return head