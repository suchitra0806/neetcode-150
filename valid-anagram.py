from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # clean the strings
        clean_s = s.lower().replace(" ", "")
        clean_t = t.lower().replace(" ", "")

        # check if the lengths are equal
        if len(clean_s) != len(clean_t):
            return False

        return Counter(clean_s) == Counter(clean_t)

        