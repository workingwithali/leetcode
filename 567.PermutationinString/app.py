from collections import Counter

def checkInclusion(s1: str, s2: str) -> bool:
    len1, len2 = len(s1), len(s2)
    
    if len1 > len2:
        return False
    
    s1_count = Counter(s1)
    s2_count = Counter(s2[:len1])
    if s1_count == s2_count:
        return True
    
    
    for i in range(len1, len2):
        s2_count[s2[i]] += 1
        # Remove the character that is no longer in the window
        s2_count[s2[i - len1]] -= 1
        
        # If the count becomes 0, remove the key from the dictionary
        if s2_count[s2[i - len1]] == 0:
            del s2_count[s2[i - len1]]
        print(s2_count)
        
        # If the current window matches s1_count, return True
        if s1_count == s2_count:
            return True
    
    return False
# Test Case 1
s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2))  # Output: True

# Test Case 2
s1 = "ab"
s2 = "eidboaoo"
print(checkInclusion(s1, s2))  # Output: False
