class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        right_list=nums[:-k]
        left_list=nums[-k:]
        nums[:]=left_list+right_list