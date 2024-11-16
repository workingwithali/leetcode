class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head):
        prev = None
        while head:
            nextp = head.next  # Store the next node
            head.next = prev   # Reverse the current node's pointer
            prev = head        # Move prev to the current node
            head = nextp       # Move head to the next node
        return prev

def create_linked_list(elements):
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    for value in elements[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(" -> ".join(map(str, values)))

# Test the code
elements = [1, 2, 3, 4]
head = create_linked_list(elements)
solution = Solution()
result = solution.reverse(head)

# Print the reversed linked list
print_linked_list(result)  # Expected output: 4 -> 3 -> 2 -> 1
