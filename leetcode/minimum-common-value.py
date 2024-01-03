class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        left = 0
        left_2 = 0
        while left < len(nums1) and left_2 < len(nums2):
            if nums1[left] == nums2[left_2]:
                return nums1[left]
            elif nums1[left] > nums2[left_2]:
                left_2 += 1
            else:
                left += 1
        return -1