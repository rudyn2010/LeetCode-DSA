class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        def backtrack(openP, closedP):
            
            #valid if and only if openP == closedP == n
            if openP == closedP == n:
                res.append("".join(stack))
                return 
            
            #only add opening paranthesis if open < n
            if openP < n:
                stack.append("(")
                backtrack(openP + 1, closedP)
                stack.pop()
              
            #only add a closing paranthesis if closed < open 
            if closedP < openP:
                stack.append(")")
                backtrack(openP, closedP + 1)
                stack.pop()
                
        backtrack(0,0)
        return res