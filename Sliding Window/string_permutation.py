class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr1 = [0] * 26
        arr2 = [0] * 26

        n = len(s1)
        m = len(s2)

        if n > m:
            return False 

        for i in range(0,n):
            arr1[ord(s1[i]) - ord('a')] += 1
            arr2[ord(s2[i]) - ord('a')] += 1

        if n == m and arr1 != arr2:
            return False
        if arr1 == arr2:
            return True

        for i in range(n, m):
            arr2[ord(s2[i-n]) - ord('a')] -= 1
            arr2[ord(s2[i]) - ord('a')] += 1

            if arr1 == arr2:
                return True
        
        return False