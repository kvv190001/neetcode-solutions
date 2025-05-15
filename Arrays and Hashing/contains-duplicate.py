class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictInt = {}

        for i in nums:
            dictInt[i] = dictInt.get(i,0) + 1
            if dictInt[i] > 1:
                return True
        
        return False