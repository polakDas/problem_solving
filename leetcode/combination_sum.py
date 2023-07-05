class Solution:
    def combinationSum(self, candidates, target):
        result = []
        self.backtrick([], candidates, target, 0, result)
        return result

    def backtrick(self, combination, candidates, target, start, result):
        if target == 0:
            result.append(combination[:])
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            combination.append(candidates[i])
            self.backtrick(combination, candidates, target - candidates[i], i, result)
            combination.pop()

if __name__=="__main__":
    candidates = [2,3,6,7]
    target = 7

    solve = Solution()
    print(solve.combinationSum(candidates, target))