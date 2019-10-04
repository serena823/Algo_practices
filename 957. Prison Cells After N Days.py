class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        history = []
        d = 0
        while d < N :
          
            day = [0] * 8
            for i in range(1, len(cells) - 1):
                if cells[i - 1] == cells[i + 1]:
                    day[i] = 1
            if day in history:
                return history[N % d - 1] 
            else:
                history.append(day)
            cells = day
            d = d + 1
        return day
        
  
        