class solution:
    def cycle(self,head):
        seen = set()
        cur = head
        while cur:
            