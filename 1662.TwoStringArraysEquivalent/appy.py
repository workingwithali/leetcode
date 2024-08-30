class solution:
    def string(self, word1,word2):
        str1 = str2 = ""
        for word in word1:
            str1 += word
        for word in word2:
            str2 += word
        return str1 == str2
solution = solution()
word1 = ['ab','c']
word2 = ['a','bc']
result = solution.string(word1 , word2)
print (result)