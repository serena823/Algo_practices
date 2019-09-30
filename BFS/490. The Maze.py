class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        if maze is None or len(maze) == 0 or len(maze[0]) == 0:
            return False
   
        queue = [start]
        while queue:
            x,y = queue.pop(0)
            maze[x][y] = 2
            
            if x == destination[0] and y == destination[1]:
                return True
            
            for delta_x, delta_y in ((0,1),(0,-1),(-1,0),(1,0)):
                xx = delta_x + x
                yy = delta_y + y
                
                while 0 <= xx < len(maze) and 0 <= yy < len(maze[0]) and maze[xx][yy] != 1:
                    xx += delta_x
                    yy += delta_y
                    
                xx = xx - delta_x
                yy = yy - delta_y
                if maze[xx][yy] == 0: 
                    queue.append([xx,yy])
                
        return False
            
        
        
        