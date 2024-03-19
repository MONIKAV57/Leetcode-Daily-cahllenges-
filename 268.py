#268 Missing number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        v=[-1]* (n+1)
        for inn in nums:
            v[inn]=inn
        for i in range(len(v)):
            if v[i]==-1:
                return i
        return 0
