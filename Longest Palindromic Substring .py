class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        if s is None:
            return None
        if len(s) == 1:
            return s
        longest = ""
        
        for i in range(len(s)):
            sub = self.helper(s, i, i)
            if len(sub) > len(longest):
                longest = sub
                    
            sub = self.helper(s, i, i + 1)
            if len(sub) > len(longest):
                longest = sub
                
        return longest
            
            
    
    def helper(self, s, left, right):
        count = 0
        while(left >= 0 and right < len(s)):
            if s[left] != s[right]:
                break
            left -= 1 
            right += 1
        return s[left + 1: right]
                
        