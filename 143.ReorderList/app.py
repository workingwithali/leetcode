
class Solution:
    def reorderList(self, head) :
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:  
            return
        
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        prev = None
        curr = slow
        while curr:
            nextp = curr.next
            curr.next = prev
            prev = curr
            curr = nextp

        
        first, second = head, prev
        while second and second.next:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
