class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if nums is None:
            return []
        
        start = 0 
        flag_zero = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                temp = nums[start]
                nums[start] = nums[i]
                nums[i] = temp
                start += 1
                flag_zero = start
                
        
        # print nums, start
        
        for j in range(start, len(nums)):
            if nums[j] == 1:
                temp = nums[start]
                nums[start] = nums[j]
                nums[j] = temp
                start += 1
        return nums
                
                
            
            