class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        
        for i , val in enumerate(nums):
            if val in differences:
                return [i, differences[val]]
            
            difference = target - val
            
            differences[difference] = i
        
        return None 
        