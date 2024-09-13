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
        s2_count[s2[i - len1]] -= 1
        
        if s2_count[s2[i - len1]] == 0:
            del s2_count[s2[i - len1]]
        print(s2_count)
        
        if s1_count == s2_count:
            return True
    
    return False
s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2))  # Output: True

s1 = "ab"
s2 = "eidboaoo"
print(checkInclusion(s1, s2))  # Output: False
