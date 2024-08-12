def productExceptSelf(nums):
    if len(nums) < 2:
            return 0

    prefix = []
    suffix = []
    i = 0
    j = len(nums) - 1
    runningPrefix = 1
    runningSuffix = 1
    while i < len(nums):
        runningPrefix *= nums[i]
        runningSuffix *= nums[j]
        prefix.append(runningPrefix)
        suffix.append(runningSuffix)
        
        i += 1
        j -= 1
        
    suffix.reverse()

    ans = []
    for i in range(len(nums)):
        if i == 0:
            prod = suffix[i + 1]
        elif i == len(nums) - 1:
            prod = prefix[len(nums) - 2]
        else:
            prod = prefix[i - 1] * suffix[i + 1]
        
        ans.append(prod)
        
    return ans