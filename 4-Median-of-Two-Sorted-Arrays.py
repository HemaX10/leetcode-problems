class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + nums2)
        n = len(nums)
        if n % 2 == 0 :
            return (float(nums[n/2]) + float(nums[(n/2) -1])) / 2
        else :
            return nums[n/2]