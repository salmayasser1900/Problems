class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        result=[]
        
        for num in range(1,n+1):
            if num%15==0:
                result.append('FizzBuzz')
            elif num%5==0:
                result.append("Buzz")
            elif num%3==0:
                result.append('Fizz')
            else:
                result.append(str(num))
                
        return result