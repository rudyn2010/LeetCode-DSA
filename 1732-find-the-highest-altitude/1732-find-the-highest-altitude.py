class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current, highest = 0, 0
        
        for x in gain:
            
            current += x
            
            if current > highest:
                highest = current
        
        return highest