from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # clean the strings
        clean_s = s.lower().replace(" ", "")
        clean_t = t.lower().replace(" ", "")
        if len(clean_s) != len(clean_t):
            return False
        return Counter(clean_s) == Counter(clean_t)