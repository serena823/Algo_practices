class Solution(object):
    #topological sorting
    # counting indegree
    # push 0 degree node to q
    # q delete node edge and other indegree - 1
    # find other 0 degree put in to q
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if prerequisites is None:
            return True
        
        edge, degree = self.helper(numCourses, prerequisites)
        count = 0
        q = collections.deque()
        for i in range(len(degree)):
            if degree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            count += 1
            for i in edge[node]:
                degree[i] -= 1
                if degree[i] == 0:
                    q.append(i)
                  
        return count == numCourses
                     
    def helper(self,num, pre):
        edge = {i:[] for i in range(num)}
        degree = [0 for i in range(num)]
        for i, j in pre:
            edge[j].append(i)
            degree[i] += 1 
        return (edge,degree)
        
        
        
        