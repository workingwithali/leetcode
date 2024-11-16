class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Sol:
    def isPalindrome(self, head):
        num = []
        # Collect values from the linked list
        while head:
            num.append(head.val)
            head = head.next  # Move to the next node
        
        # Use two-pointer technique to check for palindrome
        l, r = 0, len(num) - 1
        while l <= r:
            if num[l] != num[r]:
                return False
            l += 1
            r -= 1
        return True

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
solution = Sol()
result = solution.isPalindrome(head)
print(result)  # Expected output: True
