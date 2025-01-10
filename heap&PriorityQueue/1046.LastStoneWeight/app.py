class Solution:
    def stornes(self, stornes):
        while len(stornes)>1:
            stornes.sort()
            cur = stornes.pop()-stornes.pop()
            if cur:
                stornes.append(cur)
        return stornes[0] if stornes else 0

            
solution = Solution()
a = [4,3,9,8,7,6]
r = solution.stornes(a)
print(r)