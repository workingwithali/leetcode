class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        index = word.find(ch)
        print(index)
        if index == -1:
            return word  # ch is not found in word
        return word[:index+1][::-1] + word[index+1:]



solution = Solution()
word = "abcdefd"
ch = "d"
result = solution.reversePrefix(word, ch)
print(result)  # Output: "dcbaefd"
