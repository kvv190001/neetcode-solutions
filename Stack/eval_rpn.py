class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        for token in tokens:
            if token == "+":
                a = result.pop()
                b = result.pop()
                result.append(a+b)
            elif token == "*":
                a = result.pop()
                b = result.pop()
                result.append(a*b)
            elif token == "-":
                a = result.pop()
                b = result.pop()
                result.append(b-a)
            elif token == "/":
                a = result.pop()
                b = result.pop()
                result.append(int(b/a))
            else:
                result.append(int(token))
        
        return result[0]