def two_sum(nums, target):
  d = dict()
  a = []
  for i in range(len(nums)):
    x = target - nums[i]
    if x not in d:
      d[nums[i]] = i
    else:
      return [d[x], i]
