class solution:
    def vowel(self,s,k):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        l , cnt , res = 0, 0, 0
        for r in range(len(s)):
            cnt += 1 if s[r] in vowels else 0
            print(cnt)
            if r - l + 1 > k:
                cnt -=1 if s[l] in vowels else 0
                # print(cnt)
                l +=1
            res = max(res, cnt)
        return res






solution = solution()
s = "abciiidef"
k = 3
result = solution.vowel(s,k)
print(result)