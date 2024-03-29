class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        chars = list(s)
        l = 0
        r = len(s) - 1        

        while l < r:
            while l < r and chars[l] not in vowels:
                l += 1
            while l < r and chars[r] not in vowels:
                r -= 1
            chars[l], chars[r] = chars[r], chars[l]
            l += 1
            r -= 1
        
        return ''.join(chars)