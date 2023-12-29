#

#
#

height_list = [1,8,6,2,5,4,8,3,7]

def container_with_most_water(heights):
    res = 0
    l, r = 0, len(heights) - 1
    while l < r:
        area = (r - l) * min(heights[l], heights[r])
        res = max(res, area)
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    return res
    
result = container_with_most_water(height_list)
print(result)
