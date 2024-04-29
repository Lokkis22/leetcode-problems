class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0
    
        # sort the list
        nums.sort()

        count = 0
        j = len(nums)
        for i in range(len(nums)):
            if nums[i] == val:
                count+=1
            if nums[i] > val:
                j = i
                break

        # shift all entries after val
        for i in range(j, len(nums)):
            nums[i - count] = nums[i]
        
        return len(nums) - count