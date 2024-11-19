class solution:
    def midle(slef,head):
        slow, fast = head , head
        while fast and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

