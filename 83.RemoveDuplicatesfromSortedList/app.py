class solution:
    def remove(self,head):
        cur = head
        while cur:
            while cur.next and cur.next.va==cur.val:
                cur.next = cur.next.next
            cur = cur.next
            


