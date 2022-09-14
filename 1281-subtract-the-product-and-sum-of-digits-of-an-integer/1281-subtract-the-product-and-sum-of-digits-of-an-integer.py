class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        sum, product = 0, 1
        
        while n:
          digit = n % 10
          sum += digit
            
          product *= digit
          n //= 10
        return product - sum