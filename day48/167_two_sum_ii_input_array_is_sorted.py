# runtime: O(n^2)
# space: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if i > 0 and numbers[i] == numbers[i-1]:
                continue
            remain = target - numbers[i]
            for j in range(i+1, len(numbers)):
                if numbers[j] == remain:
                    return [i+1, j+1]
        
        return None

