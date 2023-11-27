# With this algorithm i can test all the combinations between height and width to find the max area i can achieve with the data given.



heights = [1,8,6,2,5,4,8,3,7]

def maxArea(height):
    l, r = 0, len(height) - 1
    res = 0

    while l < r:
        area = (r - 1) * min(height[l], height[r])
        res = max(res, area)
        if height[l] < height[r]:
            l += 1
        else:
            r += 1
    return res



result = maxArea(heights)
print(result)