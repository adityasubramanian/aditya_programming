'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

"""
            :type nums: List[int]
            :type k: int
            :rtype: void Do not return anything, modify nums in-place instead.
            """
            

'''
class Solution(object):
    def rotate(self, nums, k):
    	for i in range(len(nums)): 
    		nums[i+k] = nums[i]
    	return nums 
'''
Alternate Solution: 

class Solution(object):
    def rotate(self, nums, k):
    	    nums[:] = nums[len(nums)-k:] + nums[:len(nums) -k] 

'''