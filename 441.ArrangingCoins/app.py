class solution:
    def arrang(self,n):
        l, r = 0,n
        while l<=r:
            mid = (l+r)//2
            coins = mid*(mid+1)//2
            if coins == n:
                return mid
            elif coins < n:
                l = mid + 1
            else:
                r = mid -1
        return r