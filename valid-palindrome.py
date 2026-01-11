class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_string = ''
        for c in s:
            if c.isalnum():
                new_string += c.lower()
        return new_string == new_string[::-1]
        