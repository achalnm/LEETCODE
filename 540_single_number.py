#nums = [int(x) for x in input("Enter the array: ").split()]
'''
nums = [1,1,2,3,3,4,4,8,8]

left = 0
right = len(nums) - 1

while left<right:
    mid = (left+right) // 2
    
    if mid%2 == 1:
        mid = mid - 1
        
    if nums[mid] == nums[mid+1]:
        left = mid + 2
    else:
        right = mid
    

print(nums[left])
'''           
nums = [1,1,2,3,3,4,4,8,8]
res = 0

for i in nums:
    res = res ^ i

print(res)      
    

