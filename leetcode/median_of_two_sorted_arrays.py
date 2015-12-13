"""
There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

:type nums1: List[int]
:type nums2: List[int]
:rtype: float
"""
        
class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		if ((len(nums1) + len(nums2)) %2 is 1): 
			 return self.findMedian(nums1, nums2, (nums1+nums2)/2 +1 )
		return 0.5 * ( self.findMedian(nums1, nums2, (len(nums1) + len(nums2)) / 2) + self.findMedian(nums1, nums2, (len(nums1) + len(nums2)) / 2 + 1) )

    def findMedian(self,nums1,nums2, median):
        if (len(nums1) > len(nums2)):
            return self.findMedian(nums2, nums1, median)
        if (len(nums1) is 0):
            return nums2[median-1]
        if (median is 1):
            return min(nums1[1],nums2[1]) 
        PA = min(median/2, len(nums1))
        PB = median - PA 
        if (nums1[PA-1] <= nums2[PB-1]):
        	return self.findMedian(nums1[PA:], nums2, median - PA)
