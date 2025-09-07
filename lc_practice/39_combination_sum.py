# runtime: 
# space: 

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def combinationSumHelper(idx: int, combination: List[int], total: int):
            if total == target:
                res.append(combination[:])
                return

            # we can do this optimization because 2 <= candidates[i] <= 40
            if total > target:
                return

            if idx >= len(candidates):
                return

            combination.append(candidates[idx])
            combinationSumHelper(idx, combination, total+candidates[idx])
            combination.pop()
            combinationSumHelper(idx+1, combination, total)

        combinationSumHelper(0, [], 0)

        return res

