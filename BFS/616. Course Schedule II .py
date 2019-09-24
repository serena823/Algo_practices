class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        indegrees = [0 for i in range(numCourses)]
        edges = {i : [] for i in range(numCourses)}
        
        for i,j in prerequisites:
            edges[j].append(i)
            indegrees[i] += 1 
 
        
        q = collections.deque()
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                q.append(i)
        count = 0
        res = []
        while q:
            count += 1 
            course = q.popleft()
            res.append(course)
            for i in edges[course]:
                indegrees[i] -= 1 
                if indegrees[i] == 0:
                    q.append(i)
        if numCourses == count:
             return res
        else:
            return []
