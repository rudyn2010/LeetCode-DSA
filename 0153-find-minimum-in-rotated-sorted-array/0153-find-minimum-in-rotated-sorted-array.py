class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        res = nums[0]
        
        while l <= r:
            #handle case where array is sorted initially 
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])
            
            #right biased, if nums[m] is greater than # indexed at nums[l], search right sorted half 
            if nums[m] >= nums [l]:
                l = m + 1
            
            #left biased
            else:
                r = m - 1
        
        return res