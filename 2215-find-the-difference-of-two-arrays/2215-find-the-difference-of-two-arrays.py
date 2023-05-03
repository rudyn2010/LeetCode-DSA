class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        #Convert lists to sets, sets are collections that are unordered, immutable, and unindexed, no dupes 
        
        nums1Set, nums2Set = set(nums1), set(nums2)
        res1, res2 = set(), set()
        
        #Add function for sets, if the element is already present, it doesn't add any element. 
        for n in nums1:
            if n not in nums2Set:
                res1.add(n)
                
        for n in nums2:
            if n not in nums1Set:
                res2.add(n)
                
        #Convert res from sets to list using built in operators to match constraints    
        return [list(res1), list(res2)]