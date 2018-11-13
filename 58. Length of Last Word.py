class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        s = s.rstrip()
        print s
        for i in range(len(s)-1,-1,-1): 
            if s[i]!=' ':
                count+=1
            else:
                break
        return count
       
        