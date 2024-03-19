class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i,j=0,0
        com=float("inf")

        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                com=nums1[i]
                break
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return com if com!=float("inf") else -1
