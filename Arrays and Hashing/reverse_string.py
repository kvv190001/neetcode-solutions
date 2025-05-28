#151. Reverse Words in a String

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        tempS = ""
        arrString = []

        for c in s:
            if c == " ":
                if len(tempS) > 0:
                    arrString.append(tempS)
                    tempS = ""
                else:
                    continue
            else:
                tempS += c
                
        if s[-1] != " ":
            arrString.append(tempS)

        n = len(arrString)

        result = arrString[n-1]
        for i in range(n-2,-1,-1):
            result += " " + arrString[i]

        return result