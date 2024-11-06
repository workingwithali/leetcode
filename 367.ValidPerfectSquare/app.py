class solution:
    def saq(self, num):
        l, r = 0, num
        while l<=r:
            mid = (l+r)//2
            saq = mid * mid
            if saq == mid:
                return True
            elif saq < mid:
                l = mid + 1
            else:
                r = mid - 1
        return False
    
solution = solution()
num = 16
result = solution.saq