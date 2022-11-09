class Solution(object):
    def generateParenthesis(self, n):
        ans = []
        def gene(i,x,y):
            if i > x:
                 return 
            if i == 0 and x== 0:
                ans.append(y)
                return
            if i == 0:
                gene(i, x-1, y+')')
            else:
                gene(i-1, x, y+'(')
                gene(i, x-1, y+')')
            
        gene(n,n,'')
        return ans