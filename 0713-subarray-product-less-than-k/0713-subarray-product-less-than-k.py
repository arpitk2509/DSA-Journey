class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left = 0
        cp = 1
        tc = 0
        for right in range(len(nums)):
            cp *= nums[right]
            while cp >= k:
                cp //= nums[left]
                left += 1
            tc += right - left + 1
        return tc