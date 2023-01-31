class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        boolean_list = []
        greatest = max(candies)
        for i in candies:
            if extraCandies + i >= greatest:
                boolean_list.append(True)
            else:
                boolean_list.append(False)
                
        return boolean_list
            