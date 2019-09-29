class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        pivot = self.find_upper_cloest(A, target)
        print pivot
        left, right = pivot - 1, pivot
        res = []
        for _ in range(len(A)):
            if left < 0:
                res.append(A[right])
                right += 1 
            elif right == len(A):
                res.append(A[left])
                left -= 1
            else:
                if target - A[left] <= A[right] - target:
                    res.append(A[left])
                    left -= 1 
                else:
                    res.append(A[right])
                    right += 1 
        return res[:k]
                
                
    
    def find_upper_cloest(self, A, target):
        left, right = 0, len(A) - 1 
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] >=  target:
                right = mid
            else:
                left = mid
        if A[left] >= target:
            return left
        if A[right] >= target:
            return right
        return len(A)
            
 ##################################
#  binary search + two pointer
#  find the first element >= target
 #################################
                
            
            
            
