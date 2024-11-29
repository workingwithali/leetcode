class ListNode:
    def __init__(self,val=0,next=None) -> None:
        self.val = val
        self.next = next

def add(l1,l2):
    dummy = ListNode(0)
    cur = dummy