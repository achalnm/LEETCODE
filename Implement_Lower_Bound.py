'''
nums = [3,5,8,15,19]
x = 20
index = 0
for i in range(len(nums)):
    if nums[i] == x:
        print("Exact number found at index ", i)
    if nums[i] > x:
        index = i
        break
    elif nums [i] < x:
        index = i+1
        
print(index)
'''

nums = [3,5,8,15,19]
x = 4
ans = 0
left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] >= x:
        ans = mid
        right = mid - 1
        
    elif nums [mid] < x:
        left = mid + 1
        
print (ans)
        
        