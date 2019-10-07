class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        if numbers is None:
            return None
            
        numbers.sort()
        result = []
        print numbers
        
        for i in range(0, len(numbers) - 2):
            if i and numbers[i] == numbers[i - 1]:
                continue
            self.twosum(numbers, i + 1 , len(numbers) - 1, -numbers[i], result)
        return result 
            
        
    def twosum(self, numbers, left, right, target, result):
        while left < right:
            if numbers[left] + numbers[right] == target:
                result.append([-target, numbers[left],numbers[right]])
                left += 1 
                right -= 1 
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1 
                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1 
                    
            elif numbers[left] + numbers[right] < target:
                 left += 1 
            else:
                right -= 1 
        
                    
            
