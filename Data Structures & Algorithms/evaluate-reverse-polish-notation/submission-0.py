class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        op={'+':lambda a,b:a+b,'-':lambda a,b:a-b,'*':lambda a,b:a*b,'/':lambda a,b:int(a/b)}
        stack=[]
        for i in tokens:
            if i not in op:
                stack.append(i)
            else:
                b=int(stack.pop())
                a=int(stack.pop())
                c=op[i](a,b)
                stack.append(str(c))
        return int((stack.pop()))