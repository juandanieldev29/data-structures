def max_subarray(nums):
    if not nums:
        return 0
 
    max_sum = current_sum = nums[0]
 
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
 
    return max_sum

# def max_subarray(nums):
#     sum_nums = 0
#     start_index = 0
#     end_index = 1
#     largest_start = float('-inf')
#     largest_end = float('-inf')
#     is_start_set = False
#     is_end_set = True
#     for index, num in enumerate(nums):
#         if sum_nums + num > largest_start and not is_start_set:
#             start_index = index
#             largest_start = sum_nums + num
#             is_start_set = True
#             is_end_set = False
#         elif sum_nums + num > largest_end and not is_end_set:
#             end_index = index
#             largest_end = sum_nums + num
#             is_start_set = False
#             is_end_set = True
#         sum_nums += num
#         # if sum_nums < lowest:
#         #     lowest = sum_nums
#         #     lowest_index = index
#         # if sum_nums > largest:
#         #     largest = sum_nums
#         #     largest_index = index
#         # # if sum_nums < second_lowest and lowest < second_lowest and lowest_index != index:
#         # #     second_lowest = sum_nums
#         # #     second_lowest_index = index
#         # sums[index] = sum_nums
#     # print(sums)
#     return sum(nums[start_index: end_index + 1])



# Example 1: Simple case with positive and negative numbers
input_case_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result_1 = max_subarray(input_case_1)
print("Example 1: Input:", input_case_1, "\nResult:", result_1)  

# Example 2: Case with a negative number in the middle
input_case_2 = [1, 2, 3, -4, 5, 6]
result_2 = max_subarray(input_case_2)
print("Example 2: Input:", input_case_2, "\nResult:", result_2) 

# Example 3: Case with all negative numbers
input_case_3 = [-1, -2, -3, -4, -5]
result_3 = max_subarray(input_case_3)
print("Example 3: Input:", input_case_3, "\nResult:", result_3) 


"""
    EXPECTED OUTPUT:
    ----------------
    Example 1: Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
    Result: 6
    Example 2: Input: [1, 2, 3, -4, 5, 6] 
    Result: 13
    Example 3: Input: [-1, -2, -3, -4, -5] 
    Result: -1
    
"""