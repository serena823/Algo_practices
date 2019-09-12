class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l1 = len(nums1)
        l2 = len(nums2)
        res = []
        
        if l1 < l2:
            for i in nums1:
                m = self.search(nums2,i)
                if m not in res and m is not None:
                    res.append(m)
        else:
            for j in nums2:
                m = self.search(nums1,j)
                if m not in res and m is not None:
                    res.append(m)
        return res
    
    
    def search(self, n, target):
        start, end = 0 ,len(n)-1
        n.sort()
        while(start + 1 < end):
            mid = (start + end) / 2
            if n[mid] <= target:
                start = mid
            else:
                end = mid
        if n[start] == target:
            return n[start]
        if n[end] == target:
            return n[end]
        return None
        
            
      
    
       
    
        