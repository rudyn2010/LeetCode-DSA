class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #Since we are merging in place into nums1, establish pointer for where to start merging - last index in nums1
        
        last = m + n - 1
        
        #merge in reverse order, keep going until no more elements in either list
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n -1]:
                nums1[last] = nums1[m - 1]
                m -= 1
                
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
            
        #if leftover elements in nums2, fill rest of nums1 in front
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1