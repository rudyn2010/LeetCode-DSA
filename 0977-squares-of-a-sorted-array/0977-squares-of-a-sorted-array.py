class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        
        res = [0] * len(nums)
        
        f = len(nums) - 1
        
        # or while f >= 0
        while l <= r: 
            
            if abs(nums[l]) > abs(nums[r]):
                res[f] = nums[l] ** 2
                l += 1
                
            else:
                res[f] = nums[r] ** 2
                r -= 1
                
            f -= 1
                
        return res