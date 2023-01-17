class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(' : ')', '[' : ']', '{' : '}'}
        
        if len(s) % 2 != 0:
            return False

        stack = []
        
        for ele in s:
            if ele in dict.keys():
                stack.append(ele)
            else:
                if stack == []:
                    return False
                a = stack.pop()
                if ele!= dict[a]:
                    return False
        return stack == []