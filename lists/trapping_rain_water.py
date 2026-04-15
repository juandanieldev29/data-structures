############## BRUTE FORCE SOLUTION

# class Solution(object):
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         water_trapped = 0
#         for index, value in enumerate(height):
#             max_l = 0
#             max_right = 0
#             for left_index in range(index - 1, -1, -1):
#                 if height[left_index] > max_l:
#                     max_l = height[left_index]
#             for right_index in range(index + 1, len(height), 1):
#                 if height[right_index] > max_right:
#                     max_right = height[right_index]
#             result = min(max_l, max_right) - value
#             water_trapped += max(result, 0)
#         return water_trapped
        

# solution = Solution()
# water_trapped = solution.trap([0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2])
# print(water_trapped)

############## OPTIMAL SOLUTION

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water_trapped = 0
        max_l = 0
        max_r = 0
        pl = 0
        pr = len(height) - 1
        while pl < pr:
            if height[pl] <= height[pr]:
                p = height[pl]
                if max_l > p:
                    water_trapped += max_l - p
                else:
                    max_l = p
                pl += 1
            else:
                p = height[pr]
                if max_r > p:
                    water_trapped += max_r - p
                else:
                    max_r = p
                pr -= 1
        return water_trapped
        

solution = Solution()
water_trapped = solution.trap([0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2])
print(water_trapped)
