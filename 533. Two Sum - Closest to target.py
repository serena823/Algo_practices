class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        # write your code here
        if nums is None:
            return None
        
        nums.sort()
        cloestn = sys.maxsize
        cloestp = sys.maxsize
        start, end = 0, len(nums) - 1
        while (start < end):
            if nums[start] + nums[end] <= target:
                diff = abs(target - (nums[start] + nums[end]))
                if diff < cloestn:
                    cloestn = diff
                start += 1
            if nums[start] + nums[end] > target:
                diff = abs(target - (nums[start] + nums[end]))
                if diff < cloestp:
                    cloestp = diff
                end -= 1 
        return min(cloestn,cloestp)
                
