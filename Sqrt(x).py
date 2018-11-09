class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left=1
        right=x
        ans=0
        while(right>=left):
            mid=(left+right)/2
            if mid*mid >x:
                right=mid-1
            if mid*mid <= x:
                left=mid+1
                ans=mid
        return ans