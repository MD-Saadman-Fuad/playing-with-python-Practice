def maxArea(height):
    n = len(height)
    max1 = 0

    for i in range(n):

        for j in range((n - 1), i, -1):
            if height[i] <= height[j]:
                area = (height[i]) * (j - i)

            else:
                area = (height[j]) * (j - 1)

            if area > max1:
                max1 = area
            else:
                continue

    return max1


height = [1, 1]
maxArea(height)