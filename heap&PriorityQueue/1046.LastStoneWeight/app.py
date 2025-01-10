class Solution:
    def stornes(self, stornes):
        while len(stornes)>1:
            stornes.sort()
            cur = stornes.pop()-stornes.pop()
            if cur:
                stornes.append(cur)

            
