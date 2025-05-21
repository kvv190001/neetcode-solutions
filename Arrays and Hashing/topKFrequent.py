class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = {}

        for i in nums:
            numDict[i] = numDict.get(i, 0) + 1
        
        arr = []
        for num, cnt in numDict.items():
            arr.append([cnt,num])
        arr.sort(reverse=True)

        res = []
        for i in range(0,k):
            res.append(arr[i][1])
    
        return res