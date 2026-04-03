def rotate(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]

# def rotate(nums, k):
#     if len(nums) < 2:
#         return
#     for _ in range(k):
#         last_element = nums.pop()
#         nums.insert(0, last_element)
    


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print("Rotated array:", nums)


"""
    EXPECTED OUTPUT:
    ----------------
    Rotated array: [5, 6, 7, 1, 2, 3, 4]

"""