class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftProduct = [1]
        rightProduct = [1] * n
        
        for i in range (0,n-1):
            leftProduct.append(nums[i]*leftProduct[i])
        
        for i in range(n-2,-1,-1):
            rightProduct[i] = nums[i+1] * rightProduct[i+1]

        result = []
        for i in range(0,n):
            result.append(leftProduct[i] * rightProduct[i])
        
        return result