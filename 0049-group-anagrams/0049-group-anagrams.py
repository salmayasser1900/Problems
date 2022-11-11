class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for i in range (len(strs)):
            x = '' . join(sorted(strs[i]))
            if x not in d:
                d[x]=[strs[i]]
            else :
                  d[x].append(strs[i])
        return d.values()