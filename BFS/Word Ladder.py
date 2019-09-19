from collections import deque
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        distance = 0
        dict.add(end)
        q = deque([start])
        visited = set([start])
        
        while q:
            print q
            distance += 1
            for _ in range(len(q)):
                w = q.popleft()
                if w == end:
                   return distance
                visited.add(w)
                w_next = self.helper(w)
                for n in w_next:
                    if n in dict and n not in visited:
                        q.append(n)
                        visited.add(n)
        return 0
                
    
    def helper(self, word):
        s = "abcdefghijklmnopqrstuvwxyz"
        lword = []
        for i in range(len(word)):
            left = word[:i]
            right = word[i+1:]
            print left
            print right
            for char in s:
                if char == word[i]:
                    continue
                lword.append(left + char + right)
        return lword
               
        
        
