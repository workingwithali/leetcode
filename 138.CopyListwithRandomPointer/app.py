class solution:
    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random
def copy(self,head):
    if not head:
        return None
    cur = head
    while head
    new_node = Node(cur.val,cur.next)
    cur.next = new_node
    cur = new_node.next

    cur = head
    while cur:
        if cur.random:
            cur.next.random = cur.random.next
        cur = cur.next.next

    cur = head
    copy_head = head.next
    while cur:
        copy = cur.next
        cur.next = copy.next
        if copy.next:
            copy.next = copy.next.next
        
