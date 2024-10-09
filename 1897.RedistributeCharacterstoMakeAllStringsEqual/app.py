from collections import defaultdict
class solution :
    def word(self,words):

        char = defaultdict(int)
        for w in words:
            for c in w:
                char[c] +=1
        for c in char:
            if char[c] % len(words):
                return False
        return True
words = ["abc","aabc","bc"]
solution = solution()
result = solution.word(words)
print(result)