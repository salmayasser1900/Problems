class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        out = 0
        for i in range(len(nums)):
            out = out^nums[i]
        return(out)
