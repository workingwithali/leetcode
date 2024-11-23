
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:  # Handle edge cases for empty or single-node lists
            return
        
        # Step 1: Find the middle of the list
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

        # Step 3: Merge the two halves
        first, second = head, prev
        while second and second.next:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
