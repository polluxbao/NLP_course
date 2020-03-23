
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    for i in range(len(nums)):
        try:
            a = nums[i+1:].index(target-nums[i]) + i+1
        except:
            next
        else:
            if(a > 0):
                return [i, a]
    return None


def twoSum2(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i] + nums[j] == target):
                return [i, j]
    return None


print(twoSum([3,2,4], 6))

print(twoSum2([3,2,3], 6))