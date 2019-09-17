from collections import defaultdict
from collections import deque
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        # write your code here
        if len(edges) != n - 1:
            return False
        
        neighbors = defaultdict(list)
        
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
            
        visited = {}
        queue = deque()
        
        queue.append(0)
        visited[0] = True
        
        while queue:
            cur = queue.popleft()
            visited[cur] = True
            for node in neighbors[cur]:
                if node not in visited:
                    visited[node] = True
                    queue.append(node)
        return len(visited) == n
                    
                    
                
                
            
        
        
