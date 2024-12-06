from typing import List
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        bannedset = set(banned)
        recursivesum,intcount = 0,0
        for i in range(1,n+1):
            if i not in bannedset:
                if recursivesum + i <= maxSum:
                    recursivesum += i
                    intcount += 1
                else:
                    return intcount
        return intcount

sol = Solution()
print(sol.maxCount([11],7,50))
                