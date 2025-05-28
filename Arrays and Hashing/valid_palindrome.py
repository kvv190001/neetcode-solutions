# 125. Valid Palindrome
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newString = ""
        for c in s:
            if c.isalnum():
                c = c.lower()
                newString += c
        
        l = 0
        r = len(newString) - 1
        while l < r:
            if newString[l] != newString[r]:
                return False
            l += 1
            r -= 1
        
        return True