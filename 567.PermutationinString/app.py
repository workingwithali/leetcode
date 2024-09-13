from collections import Counter

def checkInclusion(s1: str, s2: str) -> bool:
    len1, len2 = len(s1), len(s2)
    
    if len1 > len2:
        return False
    
    s1_count = Counter(s1)
    s2_count = Counter(s2[:len1])
    # If the first window matches, return True
    if s1_count == s2_count:
        return True
    
    print(s1_count)
    print(s2_count)
    
    # Slide the window across s2
    for i in range(len1, len2):
        # Add the next character in the window
        s2_count[s2[i]] += 1
        print(s2_count)
        # Remove the character that is no longer in the window
        s2_count[s2[i - len1]] -= 1
        
        # If the count becomes 0, remove the key from the dictionary
        if s2_count[s2[i - len1]] == 0:
            del s2_count[s2[i - len1]]
        
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
