class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            result = []
            for char in string:
                if char != '#':
                    result.append(char)
                elif result:
                    result.pop()
            return ''.join(result)
        print(build(t))
        
        return build(s) == build(t)
solution = Solution()
print(solution.backspaceCompare("ab#c", "ad#c"))  # Output: True
print(solution.backspaceCompare("ab##", "c#d#"))  # Output: True
print(solution.backspaceCompare("a#c", "b"))      # Output: False
