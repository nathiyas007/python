def rearrange(nums):
    n = len(nums)
    result = [0] * n
    for i in range(len(nums)):
        result[i] = nums[nums[i]]
    return result
print(rearrange([4,0,2,1,3]))



# print(rearrange([1]))
# print(rearrange([2,0,1,4,5,3]))