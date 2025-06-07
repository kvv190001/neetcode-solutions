class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numDict = set(nums)

        result = 0
        for num in numDict:
            if num - 1 not in numDict:
                streak = 1
                cur = num
                while cur + 1 in numDict:
                    cur += 1
                    streak += 1
                result = max(result, streak)

        return result

