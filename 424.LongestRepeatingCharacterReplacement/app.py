class solution:
    def longest(self, s, k):
        count = {}
        res = 0
        l = 0
        max_char = 0
        for r in range(len(s)):
            count [s[r]] =1 + count[s[r],0]
            max_char = max(max_char, count[s[r]]) 



            res = max(res,r-l+1) 



# Create an instance of the Solution class
sol = Solution()

# Define the input string and k value
s = "AABABBA"
k = 1

# Call the characterReplacement function
result = sol.characterReplacement(s, k)

# Print the result
print(result)  # Output: 4
