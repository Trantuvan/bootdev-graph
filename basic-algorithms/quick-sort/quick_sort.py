def quick_sort(nums, low, high):
    if low >= high:
        return
    pivot_idx = partition(nums, low, high)
    quick_sort(nums, low, pivot_idx - 1)
    quick_sort(nums, pivot_idx + 1, high)
    
def partition(nums, low, high):
    pivot = nums[high]
    i = low
    for j in range(i, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i] 
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i

a = [9, 6, 2, 1, 8, 7]
quick_sort(a, 0, 5)
print(a)