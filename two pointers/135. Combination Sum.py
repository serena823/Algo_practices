class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        candidates = sorted(list(set(candidates))) # delete duplicate
        combinations = []
        self.dfs(candidates, 0, target, [], combinations )
        return combinations
    
    def dfs(self, candidates, index, target, combination, combinations):
        if target == 0:
            return combinations.append(list(combination))
        if target < 0:
            return []
        
        for i in range(index, len(candidates)):
            combination.append(candidates[i])
            self.dfs(candidates, i, target - candidates[i], combination, combinations)
            combination.pop()
