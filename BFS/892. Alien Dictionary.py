class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        seq = self.scanword(words)
        for i in range(len(seq)):
            seq[i] = list(seq[i])
            
        chars = self.getChars(words)
  
        edges = {char: [] for char in chars}
        degrees = {char:0 for char in chars}
        
        for i, j in seq:
            edges[i].append(j)
            degrees[j] += 1 
        print edges
        print degrees
        
        q = collections.deque()
        for char in chars:
            if degrees[char] == 0:
                q.append(char)
        print q
        s = []    
        while q:
            ss = q.popleft()
            print ss
            s.append(ss)
            for char in edges[ss]:
                degrees[char] -= 1 
                if degrees[char] == 0:
                    q.append(char)
                    print q
        return ''.join(s)
            
        
    
    
    
    def getChars(self, words):
        chars = set()
        for word in words:
            for char in word:
                chars.add(char)
        return chars
    
    def scanword(self,word):
        res = []
        for i in range(len(word) - 1):
            for j in range(min(len(word[i]),len(word[i+1]))):
                if word[i][j] == word[i+1][j]:
                    continue
                elif (word[i][j],word[i+1][j]) not in res:
                    res.append((word[i][j],word[i+1][j]))
        return res
