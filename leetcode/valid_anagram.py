subclass Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if (len(s) == len(t)):
            word_one = sorted(s)
            word_two = sorted(t)
            return word_one == word_two 
        else:
            return False 