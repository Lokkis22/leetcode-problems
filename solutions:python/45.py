def jump(nums):
    if len(nums) < 2:
        return 0
        
    jumps = [0]
    for i in range(1, len(nums)):
        nbrs = []
        j = 0
        while j < i:
            if j + nums[j] >= i:
                nbrs.append(jumps[j])
            j += 1
            
        minJumps = min(nbrs) + 1
        jumps.append(minJumps)
        
    return jumps[len(nums) - 1]