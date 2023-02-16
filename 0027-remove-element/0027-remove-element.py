class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0 
        for x in range(len(nums)):
            if nums[x] != val:
                nums[count] = nums[x]
                count += 1
                
        return count