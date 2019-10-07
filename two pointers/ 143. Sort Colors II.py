class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        # rainbow sort 
        # quick sort + merge sort 
        # if k == len(colors):
        #     return colors.sort()
        self.sort(colors, 1, k, 0, len(colors) - 1)
            
    def sort(self, colors, color_from, color_to, index_from, index_to):
        if color_to == color_from or index_to == index_from:
            return 
        color = (color_from + color_to) // 2 
  
        
        left, right = index_from, index_to
        while left <= right:
            while left <= right and colors[left] <= color:
                left += 1 
            
            while left <= right and colors[right] > color:
                right -= 1 
            
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1 
                right -= 1
    
        self.sort(colors, color_from, color, index_from, right)
        self.sort(colors, color + 1, color_to, left, index_to)

        
        
