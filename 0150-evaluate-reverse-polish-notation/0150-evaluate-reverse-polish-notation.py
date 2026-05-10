class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for i in range(len(tokens)):
            if tokens[i]=="+":
                s.append(s.pop(-2)+s.pop(-1))
            elif tokens[i]=="*":
                s.append(s.pop(-2)*s.pop(-1))
            elif tokens[i]=="-":
                s.append(s.pop(-2)-s.pop(-1))
            elif tokens[i]=="/":
                s.append(int(s.pop(-2)/s.pop(-1)))
            else:
                s.append(int(tokens[i]))
        return s[-1]
