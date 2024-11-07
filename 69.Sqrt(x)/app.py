class solution:
    def sq(self,x):
        l, r = 0 , x
        while l<=r:
            mid = (r+l)//2
            saq = mid*mid
            if saq == x:
                return mid
            elif saq<mid:
                l = mid +1
            else:
                r = mid - 1
        return r
solution = solution()