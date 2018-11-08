class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x>0:
            flag=1
        else:
            flag=-1
            print "haha"
            
        n=0
        while (flag==1) and (x>0):
            m=x%10
            n=n*10+m
            x=x/10

        
        if (flag==1) and (n==x):
            print "haha"
            return True
        else:
            return False