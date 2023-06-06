class Solution:
    def reverseWords(self, s: str) -> str:
        #using a deque here for some micro-optimazation, we can append elements from the list to the begining of the deque, saving time from appending to the end and reversing
        string_constructor = collections.deque()
        
        start, i = -1, 0
        
        while i < len(s):
            if s[i] != " ":
                start = i
                
                while i < len(s) and s[i] != " ":
                    i += 1
                    
                string_constructor.appendleft(s[start: i])
                
                i -= 1
                
            i += 1
        
        return " ".join(string_constructor)
        