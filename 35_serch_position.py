class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo,hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi)//2
            mid_num = nums[mid]
            if target == mid_num:
                return mid
            elif mid_num < target:
                lo = mid + 1
            elif mid_num > target:
                hi = mid - 1
        if mid_num < target:
            return mid + 1
        else:
            return mid