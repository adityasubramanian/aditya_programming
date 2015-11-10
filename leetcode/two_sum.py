class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                if i+j==target:
                    index1 = i+1
                    index2 = j+1
        return(index1,index2)