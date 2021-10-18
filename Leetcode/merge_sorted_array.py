class Solution:
    
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:

        for i in range(len(nums1) - 1, len(nums2) - 1, -1):
            nums1[i] = nums1[i - len(nums2)]
            
        i = 0
        l = len(nums2)
        r = 0
        
        while l < len(nums1) and r < len(nums2):
            
            if nums1[l] <= nums2[r]:
                nums1[i] = nums1[l]
                l += 1
                
            else:
                nums1[i] = nums2[r]
                r += 1
                
            i += 1
            
        
        while l < len(nums1):
            nums1[i] = nums1[l]
            i += 1
            l += 1
            
            
        while r < len(nums2):
            nums1[i] = nums2[r]
            i += 1
            r += 1