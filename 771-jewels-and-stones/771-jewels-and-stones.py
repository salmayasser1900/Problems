class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for i in range(len(stones)):
            for j in range(len(jewels)):
                if stones[i] == jewels[j]:
                    count = count + 1
        return count