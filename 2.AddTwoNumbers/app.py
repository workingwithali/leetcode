class ListNode:
    def __init__(self,val=0,next=None) -> None:
        self.val = val
        self.next = next

def add(l1,l2):
    dummy = ListNode(0)
    cur = dummy
    carry = 0
    while l1 or l2 or carry:
        sum = 0+ carry
        if l1:
            sum += l1.val
            l1 = l1.next


        if l2:
            sum += l2.val
            l2 = l2.next


        carry = sum//10
        cur = ListNode(sum%10)
        cur = cur.next
    return dummy.next
