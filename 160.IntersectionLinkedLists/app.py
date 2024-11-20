class solution:
    def inter(slef , heada, headb):
        l1 ,l2 = heada , headb
        while l1 != l2:
            l1 = l1.next if l1 else heada
            l2 = l2.next if l2 else headb
        return l1
