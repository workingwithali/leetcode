class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
        # Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        prev = None
        while slow:
            nextp = slow.next
            slow.next = prev
            prev = slow
            slow = nextp

        # Check palindrome
        left, right = head, prev
        while right:  # Only need to compare till the end of the reversed half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

# Helper function to create a linked list from a list
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
