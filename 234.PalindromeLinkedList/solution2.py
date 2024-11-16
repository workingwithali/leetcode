class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class solution:
    def isPalindrome(self , head):
        
        

def create_linked_list(elements):
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    for value in elements[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


# Test the code
elements = [1, 2, 2, 1]
head = create_linked_list(elements)
solution = Solution()
result = solution.isPalindrome(head)
print(result)  # Expected output: True