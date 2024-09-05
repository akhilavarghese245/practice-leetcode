class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        li, hi = 0, len(nums) - 1

        while li <= hi:
            mid = (li + hi) // 2
            mid_num = nums[mid]

            if mid_num == target:
                return mid
            elif mid_num < target:
                li = mid + 1
            elif mid_num > target:
                hi = mid - 1
        return -1

solution = Solution()
nums = [-1,0,3,5,9,12]
target = 10

print(solution.search(nums, target))