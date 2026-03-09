nums = [1, 3, 5, 6]
target = 2
temp = 0

for i in range(len(nums)):
    if nums[i] == target:
        print("Target found at ", i)
        break
    elif target > nums[i]:
        temp = i + 1
    else:
        print(i)
        break
    
else:
    print(temp)
    