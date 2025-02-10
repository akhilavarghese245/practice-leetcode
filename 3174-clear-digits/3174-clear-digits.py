class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = ""
        for char in s:
            if char.isdigit():
                if st:
                    st = st[:-1]
            else:
                st += char
        return st            