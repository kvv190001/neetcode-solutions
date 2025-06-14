class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        x = 0
        n = len(nums)
        result = set()
        while x < n and nums[x] <= 0:
            target = 0 - nums[x]
            l = x + 1
            h = n -1
            while l < h:
                if nums[l] + nums[h] == target:
                    result.add((nums[x], nums[l], nums[h]))
                    l += 1
                    h -= 1
                elif nums[l] + nums[h] > target:
                    h -= 1
                else:
                    l += 1
            x += 1
        
        list_result = list(result)
        return list_result

