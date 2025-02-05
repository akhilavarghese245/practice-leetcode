class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        unique_chars = set(s)
        frequencies = {s.count(char) for char in unique_chars}
        if len(frequencies) == 1:
            return True
        else:
            return False            

        