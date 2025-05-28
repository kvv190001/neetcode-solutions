class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxEnding = nums[0]
        rtype = nums[0]

        n = len(nums)

        for i in range(1,n):
            maxEnding = max(nums[i], maxEnding + nums[i])
            rtype = max(rtype, maxEnding)

        return rtype