class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictAnagram = defaultdict(list)

        for s in strs:
            temp_arr = [0] * 26
            for c in s:
                temp_arr[ord(c) - ord('a')] += 1
            dictAnagram[tuple(temp_arr)].append(s)

        return list(dictAnagram.values())