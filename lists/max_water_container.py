def get_max_water_container(heights):
    p1 = 0
    p2 = len(heights) - 1
    max_area = 0

    while p1 < p2:
        height = min(heights[p1], heights[p2])
        width = p2 - p1
        area = height * width

        max_area = max(max_area, area)
        if heights[p1] <= heights[p2]:
            p1 += 1
        else:
            p2 -= 1
    return max_area

# print(get_max_water_container([4, 8, 1, 2, 3, 9]))
print(get_max_water_container([1,8,6,2,5,4,8,3,7]))
