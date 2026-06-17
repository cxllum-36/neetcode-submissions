class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        ops=['*','/','+','-']
        for i in tokens:
            current=0
            if i not in ops: stack.append(i)
            elif i =='/':
                current=int(stack[-2])/int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(current)
            elif i =='*':
                current=int(stack[-2])*int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(current)
            elif i =='+':
                current=int(stack[-2])+int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(current)
            elif i =='-':
                current=int(stack[-2])-int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(current)

        return int(stack[-1])