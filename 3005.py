# https://leetcode.com/problems/count-elements-with-maximum-frequency/submissions/1197599902?envType=daily-question&envId=2024-03-08
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
    
        c=Counter(nums)
        maxx=[i for i in c.values()]
        m,res=max(maxx),0
        for  i in maxx:
            if i==m:
                res+=i
        return res
