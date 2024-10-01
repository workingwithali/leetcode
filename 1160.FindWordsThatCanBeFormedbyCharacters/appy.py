from collections import Counter
class solution:
    def word(self,words,chars):
        count = Counter(chars)
        res = 0
        for w in words:
            cur_word = Counter()
            good = True
            for c in w:
                cur_word[c] +=1
                if c not in count or cur_word[c] > count[c]:
                    good = False
                    break
            if good:
                res += len(w)
        return res
    
words = ["cat","bt","hat","tree"]
chars = "atach"
solution = solution()
result = solution.word(words,chars)
print(result)

