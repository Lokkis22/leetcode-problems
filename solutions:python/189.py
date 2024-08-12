def rotateArray(nums, k):
    if k == 0 or k == len(nums) or len(nums) < 2:
        return nums
    
    k = k % len(nums)

    firstPortion = nums[0:len(nums) - k]
    secondPortion = nums[len(nums) - k: len(nums)]

    rotatedArray = secondPortion + firstPortion
    return rotatedArray


def rotateArrayInPlace(nums, k):
    if len(nums) < 2 or k == 0 or k % len(nums) == 0:
        return nums
        
    nums.reverse()
    k = k % len(nums)

    i = 0
    j = k - 1
    while i < j:
        tmp = nums[j]
        nums[j] = nums[i]
        nums[i] = tmp
        i += 1
        j -= 1
        
    i = k
    j = len(nums) - 1
    while i < j:
        tmp = nums[j]
        nums[j] = nums[i]
        nums[i] = tmp
        i += 1
        j -= 1
        
    return nums