class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y=str(x)
        rev_str = y[::-1]
        if y==rev_str:
            return True
        else:
            return False