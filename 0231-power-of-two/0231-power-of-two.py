class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''
        The first line of the function checks if n is negative. If it is, then n cannot be a           power of two and the function returns False.
        The second line converts the integer n to a binary string using the bin function. For         example, bin(16) returns '0b10000'.
        The third line counts the number of '1's in the binary string using the count method.         If there is only one '1', then n is a power of two and the function returns True.             Otherwise, n is not a power of two and the function returns False.
        Overall, this solution has a time complexity of O(log n) due to the conversion to             binary string, and a space complexity of O(1).
        '''
        return False if n < 0 else bin(n).count('1') == 1