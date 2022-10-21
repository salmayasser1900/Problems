class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        cont = dict(Counter(nums))
        keys = cont.keys()
        
        for key in keys:
            if cont[key] == 1:
                ans = key
                
        return ans
        
        