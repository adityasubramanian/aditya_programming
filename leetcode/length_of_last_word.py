'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# For example,
# Given s = "Hello World",
# return 5.

 Subscribe to see which companies asked this question
'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if len(s) is 1:
        # 	return len(s)
   		if s.split() is not []:
   			return len(s.split()[len(s.split())-1])
   		return 0


