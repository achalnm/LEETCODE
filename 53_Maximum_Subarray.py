nums = [-2,1,-3,4]

max_current = nums[0]   
max_global = nums[0]   

for i in range(1, len(nums)):
    if max_current + nums[i] > nums[i]:
        max_current = max_current + nums[i]
    else:
        max_current = nums[i]

    if max_current > max_global:
        max_global = max_current

print("Maximum subarray sum is:", max_global)



'''
nums = [int(x) for x in input("Enter the array seperated by spaces: ").split()]

counter = 0
max_sum = 0
for i in range (len(nums)):
    counter = 0
    for j in range(i, len(nums)):
        counter = counter + nums[j]
        max_sum = max(max_sum, counter)
        
print(max_sum)
'''    