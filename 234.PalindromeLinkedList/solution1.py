class solution:
    def linked(self,head):
        # slow is mide of linked list 
        slow , fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse linklist
        prev = None
        while slow:
            nextp = slow.next
            slow.next = prev
            prev = slow
            slow = nextp

        # check palindrome
        l ,r = head , prev
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True

