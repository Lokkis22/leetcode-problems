def jumpGame(nums):
    gas = 0

    for num in nums:
        if gas < 0:
            return False
        if gas < num:
            gas = num
        gas -= 1
        
    return True