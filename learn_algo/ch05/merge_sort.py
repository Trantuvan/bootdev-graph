def merge_sort(nums):
    # before recurse
    if len(nums) <= 1:
        return nums  
    mid_idx = len(nums) // 2

    # recurse
    sorted_left_side = merge_sort(nums[:mid_idx])
    sorted_right_side = merge_sort(nums[mid_idx:])

    # post recurse
    return merge(sorted_left_side, sorted_right_side)
    
def merge(first, second):
    finals = []
    f,s = 0, 0

    while f < len(first) and s < len(second):
        if first[f] <= second[s]:
            finals.append(first[f])
            f += 1
        else:
            finals.append(second[s])
            s += 1
    
    # add the remains elems in first or second
    finals.extend(first[f:])
    finals.extend(second[s:])
    
    return finals
    
