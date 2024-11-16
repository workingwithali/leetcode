class sloution:
    def reverse(self , head):
        prev = None
        while head:
            nextp = head.next
            head.next = prev
            prev = head
            head = nextp

        return head