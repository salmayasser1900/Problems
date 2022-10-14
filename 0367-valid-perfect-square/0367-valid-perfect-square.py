class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l <= r:
            
            m = (l + r) // 2
            t = m * m
            
            if t == num:
                return True
            
            elif t < num:
                l = m + 1
                
            else:
                r = m - 1
                
        return False