class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        while n:
            ans += n & 1
            # print ans
            n= n >> 1
        return ans
    
        