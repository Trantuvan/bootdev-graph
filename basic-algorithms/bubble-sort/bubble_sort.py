def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - 1 - i):
          if nums[j] > nums[j + 1]:
              nums[j], nums[j + 1] = nums[j + 1], nums[j]
        # print("test", i,nums)
    return nums