class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        # i, j = 0, 0 
        # while j < len(nums):
        #     if nums[j] != 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i += 1
        #     j += 1 
    # 优化写操作
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1 
        while index < len(nums):
            nums[index] = 0
            index += 1 
            
                
