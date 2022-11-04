class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.find("LLL") != -1:
            return False
        cntA = 0
        for i in range(len(s)):
            if s[i] == 'A':
                cntA += 1
                if cntA > 1:
                    return False
        return True