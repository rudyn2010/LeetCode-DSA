class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        #sort list into ascending order 
        nums.sort()
        sum = 0
        
        #with sorted list, first number in each pair should be min 
        #this is addressed by giving the range a step of 2 
        for i in range(0, len(nums), 2):
            sum = sum + nums[i]
            
        return sum 