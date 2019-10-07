class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        # quick select 
        if not nums or n < 1 or n > len(nums):
            return None
        
        return self.partition(nums, 0, len(nums) - 1, len(nums) - n)
    
    def partition(self, nums, start, end, n):
        if start == end:
            return nums[n]
        
        left, right = start, end
        pivot = nums[(left + right) / 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1 
            while left <= right and nums[right] > pivot:
                right -= 1 
            
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1 
        if n <= right:
            return self.partition(nums, start, right, n)
        if n >= left:
            return self.partition(nums, left, end, n)
        
        return nums[n]
            
        
        
        
