class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        left, right = 0, len(nums) - 1 
        while (left + 1 < right):
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid
            if nums[mid] > nums[mid + 1]:
                right = mid
        return max(nums[left], nums[right])
        
