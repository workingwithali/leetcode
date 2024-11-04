class solution:
    def arrang(self,n):
        l, r = 0,n
        while l<=r:
            mid = (l+r)//2
            coins = mid*(mid+1)//2
            if coins == n:
                return mid
            elif 
