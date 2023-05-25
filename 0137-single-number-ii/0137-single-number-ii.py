class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_dictionary = {}
        
        for x in nums:
            if x in my_dictionary:
                my_dictionary[x] += 1
            else:
                my_dictionary[x] = 1
                
        singles = [sv for sv in my_dictionary if my_dictionary[sv] == 1]
        return singles[0]