class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count=0
        current_streak=0
        for num in nums:
            if num==1:
                current_streak+=1
                if current_streak>max_count:
                    max_count=current_streak
            else:
                current_streak=0
        return max_count