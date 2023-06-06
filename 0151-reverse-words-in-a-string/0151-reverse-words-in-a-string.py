class Solution:
    def reverseWords(self, s: str) -> str:
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
    
    #Using a Deque (Doubly Ended Queue) here for some micro-optimazation, 
    #we can append elements from the list to the begining of the container, 
    #saving time from having to append to the end and reversing.
    #By appending to elements to the left or the front of the container,
    #it'll give us the same result as reversing it in the end. 