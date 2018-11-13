class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            maxi=max(nums[i],maxi+nums[i])
            if maxi>ans:
                ans=maxi
        # print ans
        return ans
            