class solution:
    def twin(self, head):
        slow , fast =head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            nextp = slow.next
            slow.next = prev
            prev = slow 
            slow = nextp

        res= 0
        while slow:
            res = max(res,prev.val+slow.val)
