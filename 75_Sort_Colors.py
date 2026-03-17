'''
nums = [2,0,2,1,1,0]
n = len(nums)

for i in range(n):
    for j in range(n-1):  
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

print(nums)
'''

nums = [2,0,2,1,1,0]
low = 0
mid = 0
high = len(nums) - 1

while mid<=high:
    if nums[mid] == 0:
        nums[low], nums[mid] = nums[mid], nums[low]
        low = low + 1
        mid = mid + 1
    
    elif nums[mid] == 1:
        mid = mid + 1
        
    else:
        nums[mid], nums[high] = nums[high], nums[mid]
        high = high - 1
        
print(nums)
        
    
    