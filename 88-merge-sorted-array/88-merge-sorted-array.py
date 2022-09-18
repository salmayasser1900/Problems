class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_ = nums1[0:m]
        nums1[:] = [] 
        while nums1_ and nums2:
            if nums1_[0] <= nums2[0]:
                nums1.append(nums1_.pop(0))
            else:
                nums1.append(nums2.pop(0))
        if nums1_: 
            nums1 += nums1_
        else:
            nums1 += nums2
