class solution:
    def merge(slef,list1,a,b,list2):
        prev = list1
        for _ in range(a-1):
            prev = prev.next

        after = prev
        for _ in range(b-a+2):
            after = after.next

        prev.next = list2 

        tail = list2
        while tail.next:
            tail= tail.next

        tail.next = after
        return list1

