nums = [3,5,8,9,15,19]
x = 9

left = 0 
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2
    
    if (nums[mid] > x):
        ans = mid
        right = mid - 1
    elif (nums[mid] <= x):
        left = mid + 1

print(ans)
    