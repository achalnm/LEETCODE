#nums = [int(x) for x in input("Enter the array: ").split()]
#target = int(input("Enter the sum target: "))


nums = [10, 5, 2, 7, 1, 9]
target = 15

print("Your array is: ", nums)
print("Your sum target is: ", target)

current_sum = 0  
fest = 0          
start = 0         

for end in range(len(nums)):
    current_sum += nums[end]  

    while current_sum > target and start <= end:
        current_sum -= nums[start]
        start += 1

    if current_sum == target:
        fest = max(fest, end - start + 1)

print("Longest sub-array length:", fest)

'''
nums = [10, 5, 2, 7, 1, 9]
target = 15

print("Your array is: ", nums)
print("Your sum target is: ", target)

counter = 0
count = 0
fest = 0
start = 0  

for i in range(len(nums)):
    counter = counter  +  nums[i]
    count = count + 1

    
    while counter > target and start <= i:
        counter = counter - nums[start]
        count = count - 1
        start = start + 1

    if counter == target:
        if count > fest:
            fest = count

print(fest)  
'''    
'''
nums = [10, 5, 2, 12, 1, 9]
target = 15905

print("Your array is: ", nums)
print("Your sum target is: ", target)
counter = 0
count = 0
fest = 0
for i in range(len(nums)):
    counter = 0
    count = 0
    for j in range(i, len(nums)):
        counter = counter + nums[j]
        if(counter == target):
            count = j - i + 1
            fest = max(fest,count)
print(fest)
'''

