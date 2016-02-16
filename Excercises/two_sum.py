def two_sum(nums, target):
  for i in range(len(nums)):
    first_sum = nums[i]
    for j in range(i+1, len(nums)):
      total = first_sum + nums[j]
      if target == total:
        return [i, j]


print (two_sum([5, 1, 2, 3, 4], 3))