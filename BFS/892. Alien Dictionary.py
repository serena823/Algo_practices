# 892. Alien Dictionary
#  
# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

# Example
# Example 1:

# Input：["wrt","wrf","er","ett","rftt"]
# Output："wertf"
# Explanation：
# from "wrt"and"wrf" ,we can get 't'<'f'
# from "wrt"and"er" ,we can get 'w'<'e'
# from "er"and"ett" ,we can get 'r'<'t'
# from "ett"and"rtff" ,we can get 'e'<'r'
# So return "wertf"

# Example 2:

# Input：["z","x"]
# Output："zx"
# Explanation：
# from "z" and "x"，we can get 'z' < 'x'
# So return "zx"

# Notice
# 1.You may assume all letters are in lowercase.
# 2.You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
# 3.If the order is invalid, return an empty string.
# 4.There may be multiple valid order of letters, return the smallest in normal lexicographical order

from heapq import heappush, heappop, heapify
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        graph = self.build_graph(words)
        return self.topological_sort(graph)
    
    def build_graph(self, words):
        graph = {}
        
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set()
        
 
        # for i in range(len(words) - 1):
        #     for j in range(min(len(word[i]),len(word[i + 1]))):
        #         if word[i][j] != word[i + 1][j]:
        #             graph[word[i][j]].add(word[i + 1][j])
        #             break
        # return graph
        
        n = len(words)
        for i in range(n - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].add(words[i + 1][j])
                    break
                
        return graph
    
    def topological_sort(self, graph):
        indegree = {node: 0 for node in graph}
        for node in graph:
            for neighbour in graph[node]:
                indegree[neighbour] += 1 
        
        queue = [node for node in graph if indegree[node] == 0]
        heapify(queue)
        
        topo_order = ""
        
        while queue:
            node = heappop(queue)
            topo_order += node 
            for neighbour in graph[node]:
                indegree[neighbour] -= 1 
                if indegree[neighbour] == 0:
                    heappush(queue,neighbour)
        if len(topo_order) == len(graph):
            return topo_order
        return ""
    
    
    
# class Solution:
#     """
#     @param words: a list of words
#     @return: a string which is correct order
#     """
#     def alienOrder(self, words):
#         # Write your code here
#         seq = self.scanword(words)
#         for i in range(len(seq)):
#             seq[i] = list(seq[i])
            
#         chars = self.getChars(words)
  
#         edges = {char: [] for char in chars}
#         degrees = {char:0 for char in chars}
        
#         for i, j in seq:
#             edges[i].append(j)
#             degrees[j] += 1 
#         print edges
#         print degrees
        
#         q = collections.deque()
#         for char in chars:
#             if degrees[char] == 0:
#                 q.append(char)
#         print q
#         s = []    
#         while q:
#             ss = q.popleft()
#             print ss
#             s.append(ss)
#             for char in edges[ss]:
#                 degrees[char] -= 1 
#                 if degrees[char] == 0:
#                     q.append(char)
#                     print q
#         return ''.join(s)
            
        
    
    
    
#     def getChars(self, words):
#         chars = set()
#         for word in words:
#             for char in word:
#                 chars.add(char)
#         return chars
    
#     def scanword(self,word):
#         res = []
#         for i in range(len(word) - 1):
#             for j in range(min(len(word[i]),len(word[i+1]))):
#                 if word[i][j] == word[i+1][j]:
#                     continue
#                 elif (word[i][j],word[i+1][j]) not in res:
#                     res.append((word[i][j],word[i+1][j]))
#         return res
