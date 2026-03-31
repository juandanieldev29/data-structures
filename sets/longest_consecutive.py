def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest_sequence = 0
    
    for num in nums:
        if num - 1 not in num_set:
            current_num = num
            current_sequence = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1
            
            longest_sequence = max(longest_sequence, current_sequence)
    
    return longest_sequence

# def longest_consecutive_sequence(nums):
#     set_nums = set(nums)
#     longest_consecutive = 0
#     for num in nums:
#         consecutive = 1
#         while num + consecutive in set_nums:
#             consecutive += 1
#         if consecutive > longest_consecutive:
#             longest_consecutive = consecutive
#     return longest_consecutive


print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""
