class Solution(object):
    def merge(self, nums1, m, nums2, n):
        #  go backwards and fill the array
        while m > 0 and n > 0:
            if (nums2[n - 1] > nums1[m - 1]):
                nums1[m + n - 1] = nums2[n - 1]
                n-=1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m-=1
        
        # if nums1 got completed first, fill out the rest of nums1
        if (m <= 0):
            while n > 0:
                nums1[n - 1] = nums2[n - 1]
                n-=1
        
        # if nums2 got completed first, we are done