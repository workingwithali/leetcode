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