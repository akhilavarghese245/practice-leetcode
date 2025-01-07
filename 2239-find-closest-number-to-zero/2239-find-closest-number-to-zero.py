class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dist = nums[0]
        for i in nums:
            if abs(i) < abs(dist):
                dist = i

        if dist < 0 and abs(dist) in nums:
            return abs(dist)
        else:
            return dist             
            