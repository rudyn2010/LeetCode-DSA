class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.strip()
        lis = list(string.split(" "))
        return len(lis[-1])