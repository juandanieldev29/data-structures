def remove_duplicates(nums):
    dups = {}
    length_unique = 0
    index_last_unique = 0
    for index, num in enumerate(nums):
        if num not in dups:
            temp = nums[index]
            nums[index] = nums[index_last_unique]
            nums[index_last_unique] = temp
            index_last_unique += 1
            dups[num] = index
            length_unique += 1
    return index_last_unique

test4 = [1, 1, 2, 2, 3, 4, 5, 5]
print(f"Test 4 Before: {test4}")
result4 = remove_duplicates(test4)
print(f"Test 4 After: {test4[:result4]}")
print(f"New Length: {result4}")
print("------")