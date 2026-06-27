class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left=0
        cp=1
        tc=0
        if k<=1:
            return 0
        else:
            for right in range(len(nums)):
                cp=cp*nums[right]
                while cp>=k:
                    cp/=nums[left]
                    left+=1
                tc += right - left + 1
        return tc