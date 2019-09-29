class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        if n < 0:
            return 1 / self.helper(x, -n)
        else:
            return self.helper(x, n)
    
    def helper(self, x, n):
        if n == 0:
            return 1 
        half = self.helper(x , n / 2)
        
        if n % 2 == 0:
            return half * half 
        else:
            return half * half * x 