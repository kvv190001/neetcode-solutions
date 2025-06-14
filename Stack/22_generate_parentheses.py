class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def parenthesis(n, pOpen, pClose, curStr):
            if pOpen == n:
                if pOpen == pClose:
                    result.append(curStr)
                else:
                    curStr += ')'
                    parenthesis(n, pOpen, pClose + 1, curStr)
            else:
                parenthesis(n,pOpen + 1, pClose, curStr + '(')
                if pOpen > pClose:
                    parenthesis(n, pOpen, pClose + 1, curStr + ')')
            return

        parenthesis(n, 0, 0, "")

        return result