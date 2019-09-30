#class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a 
# bad version.
class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        left, right = 1, n 
        while left + 1 < right:
            mid = (left + right) / 2
            if SVNRepo.isBadVersion(mid) is False:
                left = mid
            else:
                right = mid
        if SVNRepo.isBadVersion(left) is True:
            return left
        if SVNRepo.isBadVersion(right) is True:
            return right
        return -1
        