class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        k = 1
        for i in range(len(nums)):
            if i == 0 or nums[i] == nums[i - 1]:
                continue
            else:
                nums[k] = nums[i]
                k+=1
        return k

sol = Solution()
nums = [1,1,2]
nums2 = [0,0,1,1,1,2,2,3,3,4]

print(sol.removeDuplicates(nums))
print(nums)

print(sol.removeDuplicates(nums2))
print(nums2)