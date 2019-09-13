class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res2 = []
        for i in range(len(nums)-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            res2.extend(self.findtwo(nums[i],nums[i+1:]) )
        return res2
            
        
        
    def findtwo(self, s, nums):
        res = []
        
        start, end = 0, len(nums) - 1
        
        if nums[0] + nums[1] > -s or nums[len(nums) - 1] + nums[len(nums) -2 ] < -s:
            return res
        while(start < end):
            if start != 0 and nums[start] == nums[start-1]:
                start += 1
                continue
            if nums[start] + nums[end] < -s:
                start += 1
            elif nums[start] + nums[end] > -s:
                end -= 1
            elif nums[start] + nums[end] == -s:
                res.append([nums[start], nums[end], s])
                start += 1
        return res
                
                
        
            
        